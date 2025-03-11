FROM public.ecr.aws/lambda/python:3.13

# Copy requirements and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install --target=/var/task -r requirements.txt

# Copy Lambda function
COPY ./src/lambda2.py ${LAMBDA_TASK_ROOT}

# Set the Lambda handler
CMD ["lambda2.handler"]
