import boto3
import os

UserSub = 'b38af617-b340-4ea3-ba4f-e3da1f1e8c52'

s3 = boto3.resource(
    's3',
    region_name=os.getenv('COGNITO_REGION_NAME'),
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('ACCESS_KEY')
)
content="String content to write to a new S3 file"
s3.Object('www.projectfit.com', 'newfile.txt').put(Body=UserSub)