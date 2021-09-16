This is a sample userapp api service collection for managing user account. 
Below are the important methods and the user model:

User
-   UserId
-   Email
-   FirstName
-   LastName
-   Password


1. getusers - Get all the users
endpoint:   https://igrp4yzg2m.execute-api.us-east-1.amazonaws.com/dev/users/

2. getuserbyid - Get user by userId
endpoint:   https://igrp4yzg2m.execute-api.us-east-1.amazonaws.com/dev/users/<userId>

3. createuser - Adding new user
endpoint:   https://igrp4yzg2m.execute-api.us-east-1.amazonaws.com/dev/users/
Sample request body:
{
    "userId": "1001",
    "email": "test.user1001@gmail.com",
    "firstName": "Test",
    "lastName": "User1001",
    "password": "user1001"
}

4. updateemailbyid - Update email by userId
endpoint:   https://igrp4yzg2m.execute-api.us-east-1.amazonaws.com/dev/users/
{
    "userId": "1001",
    "email": "test.user1001@gmail.com"
}

5. deleteuser - Delete User by userId
endpoint:   https://igrp4yzg2m.execute-api.us-east-1.amazonaws.com/dev/users/<userId>



Postman collection public link:
https://www.getpostman.com/collections/a6df4ce80a19cfd80d98
Note: Please make sure the base url variable are set before running the collection