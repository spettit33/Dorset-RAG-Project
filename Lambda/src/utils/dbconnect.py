from dotenv import load_dotenv
import redis
import os

load_dotenv();

def connectToDatabase():

    username = os.environ['REDIS_USERNAME'];
    password = os.environ['REDIS_PASSWORD'];

    redisCache = redis.Redis(
        host='redis-17027.c338.eu-west-2-1.ec2.redns.redis-cloud.com',
        port=17027,
        decode_responses=True,
        username=username,
        password=password,
    );

    return redisCache;

class redisCache:
    def __init__(self):
        pass;
    def __enter__(self):
        self.client = connectToDatabase();
        return self.client;
    
    def __exit__(self,exc_type, exc_value, traceback):
        if self.client:
            self.client.close();

if (__name__ == "__main__"):
    connectToDatabase();