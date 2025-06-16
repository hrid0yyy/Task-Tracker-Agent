from mongoclient import get_collection

def insert_document(db_name: str, collection_name: str, document: dict):
    """
    Inserts a document into the specified MongoDB collection.
    
    :param db_name: Name of the database
    :param collection_name: Name of the collection
    :param document: Document to be inserted
    :return: Inserted document ID
    """
    collection = get_collection(db_name, collection_name)
    result = collection.insert_one(document)
    return result.inserted_id


def find_document(db_name: str, collection_name: str, query: dict):
    """
    Finds a document in the specified MongoDB collection based on the query.
    
    :param db_name: Name of the database
    :param collection_name: Name of the collection
    :param query: Query to find the document
    :return: Found document or None if not found
    """
    collection = get_collection(db_name, collection_name)
    return collection.find(query)

def update_document(db_name: str, collection_name: str, query: dict, update: dict):
    """
    Updates a document in the specified MongoDB collection based on the query.
    
    :param db_name: Name of the database
    :param collection_name: Name of the collection
    :param query: Query to find the document to update
    :param update: Update operations to be applied
    :return: Number of documents updated
    """
    collection = get_collection(db_name, collection_name)
    result = collection.update_one(query, update)
    return result.modified_count

def delete_document(db_name: str, collection_name: str, query: dict):
    """
    Deletes a document from the specified MongoDB collection based on the query.
    
    :param db_name: Name of the database
    :param collection_name: Name of the collection
    :param query: Query to find the document to delete
    :return: Number of documents deleted
    """
    collection = get_collection(db_name, collection_name)
    result = collection.delete_one(query)
    return result.deleted_count