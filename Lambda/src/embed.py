import boto3
import json
import openai
import os
from langchain.vectorstores import PineconeVectorStore
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def handler(event, context):
    openai.api_key = os.environ['OPENAI_API_KEY'];
    pcApiKey = os.environ['PINECONE_API_KEY'];
    pcIndexName = os.environ['PINECONE_INDEX_NAME'];

    s3_client = boto3.resource('s3');
    bucket_name = event['Records'][0]['s3']['bucket']['name'];
    file_key = event['Records'][0]['s3']['object']['key'];
    response = s3_client.head_object(Bucket=bucket_name, Key=file_key);

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024);
    pcVectorStore = PineconeVectorStore.from_existing_index(pcIndexName, embeddings);

    file = s3_client.get_object(Bucket=bucket_name, Key=file_key);
    content = file['Body'].read().decode('utf-8');

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50);
    chunks = text_splitter.split_text(content);

    metadata = {"Document": file_key, "Person": response['Metadata']['Person'], "Role": response['Metadata']['Role'], "Date": response['Metadata']['Date']};

    for i, chunk in enumerate(chunks):
        chunk.metadata = metadata;

    pcVectorStore.add_documents(chunks);

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Document processed and embeddings stored successfully.'
        })
    }


if (__name__ == "__main__"):
    print(handler("hi","context"));