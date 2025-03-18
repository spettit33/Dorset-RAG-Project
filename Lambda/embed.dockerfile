FROM public.ecr.aws/lambda/python:3.12

# Copy requirements and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip cache purge

RUN pip install \
--platform manylinux2014_x86_64 \
--target=/var/task \
--implementation cp \
--python-version 3.12 \
--no-cache-dir \
--only-binary=:all: --upgrade \
-r requirements.txt

# Copy Lambda function
COPY ./src/embed.py ${LAMBDA_TASK_ROOT}

# Set the Lambda handler
CMD ["embed.handler"]