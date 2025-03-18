FROM public.ecr.aws/lambda/python:3.12

# Copy requirements and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip cache purge

RUN pip install \
--platform manylinux2014_x86_64 \
--target=/var/task \
--implementation cp \
--python-version 3.12 \
--only-binary=:all: --upgrade \
-r requirements.txt

COPY ./src/utils ${LAMBDA_TASK_ROOT}/utils

# Copy Lambda function
COPY ./src/query.py ${LAMBDA_TASK_ROOT}

# Set the Lambda handler
CMD ["query.handler"]
