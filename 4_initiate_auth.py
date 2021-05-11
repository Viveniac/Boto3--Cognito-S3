import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username = 'vivekanand.kulkarni@resmed.com'
password = '#1234Abc'

client = boto3.client('cognito-idp',region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.initiate_auth(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    AuthFlow = 'USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
    }
)
# print(response)
# print('AccessToken:',response['AuthenticationResult']['AccessToken'])
# print('RefreshToken:',response['AuthenticationResult']['RefreshToken'])

access_token = response['AuthenticationResult']['AccessToken']

client = boto3.client('cognito-idp',region_name= os.getenv('COGNITO_REGION_NAME'))
response2 = client.get_user(
    AccessToken = access_token
)

# print(response)
attr_sub = None
for attr in response2['UserAttributes']:
    if attr['Name'] =='sub':
        attr_sub = attr['Value']
        break

print('UserSub', attr_sub)