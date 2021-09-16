This is a sample userapp api service collection for managing user account. 
Below are the important methods and the user model:

User
-   UserId
-   Email
-   FirstName
-   LastName
-   Password

base_url: https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev

1. getusers - Get all the users
endpoint:   base_url/users/

2. getuserbyid - Get user by userId
endpoint:   base_url/users/<userId>

3. createuser - Adding new user
endpoint:   base_url/users/
Sample request body:
{
    "userId": "1001",
    "email": "test.user1001@gmail.com",
    "firstName": "Test",
    "lastName": "User1001",
    "password": "user1001"
}

4. updateemailbyid - Update email by userId
endpoint:   base_url/users/
{
    "userId": "1001",
    "email": "test.user1001@gmail.com"
}

5. deleteuser - Delete User by userId
endpoint:   base_url/users/<userId>

