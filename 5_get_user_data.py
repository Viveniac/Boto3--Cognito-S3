import os
import boto3
from dotenv import load_dotenv
load_dotenv()

access_token = response['AuthenticationResult']['AccessToken']

client = boto3.client('cognito-idp',region_name= os.getenv('COGNITO_REGION_NAME'))
response = client.get_user(
    AccessToken = access_token
)

# print(response)
attr_sub = None
for attr in response['UserAttributes']:
    if attr['Name'] =='sub':
        attr_sub = attr['Value']
        break

print('UserSub', attr_sub)