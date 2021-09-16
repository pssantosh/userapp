import os

import boto3
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

# dynamodb_client = boto3.client('dynamodb')

# if os.environ.get('IS_OFFLINE'):
#     dynamodb_client = boto3.client(
#         'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
#     )

USERS_TABLE = os.environ['USERS_TABLE']


# Get all users
@app.route('/users/')
def getusers():

    dynamodb = boto3.resource('dynamodb')    
    table = dynamodb.Table(USERS_TABLE)

    response = table.scan()
    items = []

    for i in response['Items']:
        items.append(i)

    return  make_response(jsonify(items), 200)


# Get user by userId
@app.route('/users/<string:user_id>')
def getuserbyid(user_id):

    dynamodb = boto3.resource('dynamodb')    
    table = dynamodb.Table(USERS_TABLE)

    resp = table.get_item(
            Key={'userId': user_id}
        )
    
    if 'Item' in resp:
        return make_response(jsonify(resp['Item']), 200)
    else:
        return make_response(jsonify(error='User not found!'), 404)


#Delete User by userId
@app.route('/users/<string:user_id>', methods=['DELETE'])
def deleteuser(user_id):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(USERS_TABLE)

    response = table.delete_item(Key={'userId': user_id})

    return make_response(jsonify(success='user deleted!'), 200)


#Add user
@app.route('/users', methods=['POST'])
def createuser():

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(USERS_TABLE)

    user_id = str(request.json.get('userId'))
    email = request.json.get('email')
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    password = request.json.get('password')

    if not user_id or not email:
        return make_response(jsonify(error='userId and email are required!'), 400)

    user_info={
        'userId': user_id,
        'email': email,
        'firstName': first_name,
        'lastName': last_name,
        'password': password
    }

    table.put_item(Item=user_info)

    return make_response(jsonify(success='user created!'), 201)

#Update email by user id
@app.route('/users', methods=['PUT'])
def updateemailbyid():

    user_id = request.json.get('userId')
    email = request.json.get('email')

    if (userexists(user_id)):
        dynamodb = boto3.resource('dynamodb')    
        table = dynamodb.Table(USERS_TABLE)

        table.update_item(
            Key={
                'userId': user_id
                },
            UpdateExpression="set email = :e",
            ExpressionAttributeValues={
                    ':e': email
                },
        ReturnValues="UPDATED_NEW"
        )
        return make_response(jsonify(success='update successful!'), 200)
    else:
        return make_response(jsonify(error='invalid userId!'), 400)


#Check if user already exists
def userexists(user_id):
    
    dynamodb = boto3.resource('dynamodb')    
    table = dynamodb.Table(USERS_TABLE)

    resp = table.get_item(
            Key={'userId': user_id}
        )
    
    if 'Item' in resp:
        return True
    else:
        return False


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='not found!'), 404)
