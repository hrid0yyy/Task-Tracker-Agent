from crud import insert_document, find_document, update_document, delete_document

db = "TTA"
collection = "tasks"


query = {"name": "Alice"}
response = find_document(db, collection, query) # Find document by name
for doc in response:
    print(doc)