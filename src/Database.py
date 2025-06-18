from pymongo import MongoClient
from dotenv import load_dotenv
import os
from Task import TaskClass
import uuid
from typing import Union


load_dotenv()  
client = MongoClient(os.getenv('MONGODB_ATLAS_KEY'))
db = client[os.getenv('MONGODB_DATABASE_NAME')]
tasks_collection = db['tasks']

def add_to_task(task: TaskClass):
    """
    Adds a task to the MongoDB database.
    """
    task = task.to_dict()
    tasks_collection.insert_one(task)
    return f"Task Id : '{task['_id']}', description : '{task['description']}' added successfully."

def get_all_tasks():
    """
    Retrieves all tasks from the MongoDB database.
    """
    tasks = list(tasks_collection.find())
    if not tasks:
        return "No tasks found."
    response = ""
    for task in tasks:
        task = TaskClass(
            _id=task['_id'],
            description=task['description'],
            deadline=task['deadline'],
            created_at=task['created_at'],
            updated_at=task['updated_at'],
            completed=task['completed']
        )
        response += task.format() 

    return response


def get_task_by_id(task_id: Union[str, uuid.UUID]):
    """
    Retrieves a task by its ID from the MongoDB database.
    """
    if isinstance(task_id, uuid.UUID):
        task_id = str(task_id)
    # find by mongo object id
    try:
        task = tasks_collection.find_one({"_id": task_id})
        if task is None:
            return "Task not found."
        return TaskClass(
             _id=task['_id'],
            description=task['description'],
            deadline=task['deadline'],
            created_at=task['created_at'],
            updated_at=task['updated_at'],
            completed=task['completed']
        )
    except Exception as e:
        return f"Invalid ObjectId"

def update_task(task_id: str, updated_task: TaskClass):
    """
    Updates a task in the MongoDB database.
    """
    try:
        result = tasks_collection.update_one(
            {"_id": task_id},
            {"$set": updated_task.to_dict()}
        )
        if result.matched_count == 0:
            return "Task not found."
        return f"Task with ID '{task_id}' updated successfully."
    except Exception as e:
        return f"Error updating task: {str(e)}"
    

def delete_all_tasks():
    """
    For Clearance:
    Deletes all tasks from the MongoDB database.
    """
    tasks_collection.delete_many({})
    return "All tasks deleted successfully."
   
