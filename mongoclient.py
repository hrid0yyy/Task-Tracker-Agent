from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  

MONGODB_ATLAS_KEY = os.getenv('MONGODB_ATLAS_KEY')

client = MongoClient(MONGODB_ATLAS_KEY)

def get_collection(db_name: str, collection_name: str) -> MongoClient:
    """
    Returns a MongoDB collection from the specified database and collection name.
    """
    return client[db_name][collection_name]

