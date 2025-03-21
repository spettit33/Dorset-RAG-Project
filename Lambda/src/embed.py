import boto3
import json
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from uuid import uuid4

def handler(event, context):
    print("before envs")
    pcApiKey = os.environ['PINECONE_API_KEY'];
    pcIndexName = os.environ['PINECONE_INDEX_NAME'];
    hfEmbeddingApiKey = os.environ['HF_API_KEY']
    print("after envs");
    try:
        s3_client = boto3.client('s3');
    except Exception as e:
        print(e);
    else:
        print("all good");
    print(s3_client);
    bucket_name = event['Records'][0]['s3']['bucket']['name'];
    print(bucket_name);
    file_key = event['Records'][0]['s3']['object']['key'];
    print(file_key);
    response = s3_client.head_object(Bucket=bucket_name, Key=file_key);
    print(response);

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    print(embeddings);
    pcVectorStore = PineconeVectorStore.from_existing_index(pcIndexName, embeddings);

    file = s3_client.get_object(Bucket=bucket_name, Key=file_key);
    content = file['Body'].read().decode('utf-8');

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50);
    chunks = text_splitter.split_text(content);

    metadata = {"Document": file_key, "person": response['Metadata']['person'], "role": response['Metadata']['role'], "date": response['Metadata']['date']};
    documents = [];

    print(chunks);

    for i, chunk in enumerate(chunks):
        documents.append(Document(page_content=chunk, metadata=metadata, index=i));
    
    uuids = [str(uuid4()) for i in range(len(documents))];

    print(documents);

    pcVectorStore.add_documents(documents, ids = uuids);

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Document processed and embeddings stored successfully.'
        })
    }


if (__name__ == "__main__"):
    print(handler("hi","context"));