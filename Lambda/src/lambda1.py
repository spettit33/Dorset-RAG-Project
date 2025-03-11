import boto3

def handler(event, context):
    print(event);
    dynamodb = boto3.resource('dyanmodb');
    table = dynamodb.create_table(
        TableName='users'
    )
    return 'Hello from Lambda!'


if (__name__ == "__main__"):
    print(handler("hi","context"));