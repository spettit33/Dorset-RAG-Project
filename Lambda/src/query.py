from utils.dbconnect import redisCache

def handler(event, context):
    print(redisCache);

    with redisCache() as r:
        print(r);
        r.set('foo', 'bar');
        value = r.get('foo');
        print(value);
    return f"I am testing whether dependencies work in aws lambda - the shape of my array is 3!"


if (__name__ == "__main__"):
    print(handler("hi","context"));