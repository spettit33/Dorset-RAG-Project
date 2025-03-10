import boto3

def lambda_handler(event, context):
    print(event);
    dynamodb = boto3.resource('dyanmodb');
    table = dynamodb.create_table(
        TableName='users'
    )
    return 'Hello from Lambda!'


if (__name__ == "__main__"):
    print(lambda_handler("hi","context"));