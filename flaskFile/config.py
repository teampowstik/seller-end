
from azure.storage.blob import BlobServiceClient
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

PSWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

load_dotenv()


PRODUCT_DATABASE = os.getenv(r'PRODUCT_DATABASE')
SECRET_KEY = os.getenv('SECRET_KEY')
CONNECTION_STRING = os.getenv('CONNECT_STRING')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')
IMAGE_SIZE = os.getenv('IMAGE_SIZE')

class Config:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = PRODUCT_DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def get_client():
    conn_str = CONNECTION_STRING
    container = CONTAINER_NAME
    blob_service_client = BlobServiceClient.from_connection_string(conn_str = conn_str)
    container_service_client = blob_service_client.get_container_client(container=container)
    container_service_client.get_container_properties()
    return container_service_client
