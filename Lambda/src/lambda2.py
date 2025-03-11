import numpy as np

def handler(event, context):
    a = np.array([1,2,3]);
    return f"I am testing whether dependencies work in aws lambda - the shape of my array is {a.shape}!"


if (__name__ == "__main__"):
    print(handler("hi","context"));