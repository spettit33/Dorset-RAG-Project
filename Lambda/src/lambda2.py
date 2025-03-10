def lambda_handler(event, context):
    return f"Hello from Lambda {event}!"


if (__name__ == "__main__"):
    print(lambda_handler("hi","context"));