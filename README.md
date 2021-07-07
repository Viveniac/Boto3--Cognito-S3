# Boto3--Cognito-S3
Python script to automate Cognito authentication and S3 configuration


1.1. Sign_up Script
The purpose of this script is to create a User sign up and populate it in Cognito-identity pool and this also sends a confirmation email to the user.

Confirmation email can be either a link or confirmation code.

sign_up api is used requires necessary fields:

ClientId:  Cognito user client Id of the Cognito AWS service
Username: Sign up username(Email address)
Password: Password to be created as per pool requirement.
1.2. Confirm_sign_up Script
Here we make use of credentials provided by the User for User sign up and if the confirmation email contains code, then retrieving the code we need to confirm the sign up.

confirm_sign_up api is used which requires these necessary fields:

ClientId:  Cognito user client Id of the Cognito AWS service
Username: Sign up username(Email address)
Confirmation Code: Confirmation code sent to the user.
This step can be avoided if we make use of the pool which uses link in the email as a confirmation means.

1.3. Initiate_Authentication, Get User Data and a Create S3 File for that user Script
Here we initiate an authentication flow using the sign up user credentials which gives us Authentication result and access token and the data in which we are interested here is the access token data which is specific to each user, using this we get the User data, from the user data, in the data the UserSub value is the created AWS credentials specific to each user after authentication.

initiate_auth api is used which requires these necessary fields:

ClientId:  Cognito user client Id of the Cognito AWS service
AuthFlow: The authentication flow for this call to execute. The API action will depend on this value of 'USER_PASSWORD_AUTH' in this script which is Username and Password
AuthParameters: Since we are using USER_PASSWORD_AUTH, we pass in these values as parameters here.
get_user api is used which requires these necessary fields:

AccessToken: Pass the access token created in the Authentication Result
The UserSub which collect from the results of get_user api is the unique User data which we want to use and AWS credentials and create a S3 File in the bucket linked.

Make use of the following APIs

boto3.resource with the following necessaries passed in as the arguments 

S3
region_name
aws_access_key_id
aws_secret_access_key
.object(bucketname,filename.fileformat ).put(Body='data to be stored') with the following as the necessary arguments
