import uuid
from Task import TaskClass
from datetime import datetime
from langchain_core.tools import tool
from Database import add_to_task, get_all_tasks, get_task_by_id, delete_all_tasks, update_task
from langchain_community.tools import DuckDuckGoSearchRun

ddg = DuckDuckGoSearchRun()

@tool
def add_task(description: str, deadline: str = None) -> str:
    """
    Adds a new task to the database with the given description and optional deadline.
    Create a description from the user input.
    If user provides no deadline, it will be set to None.

    Args:
        description (str): The description of the task.
        deadline (str, optional): The deadline for the task in ISO format. Defaults to None.
    
    Returns:
        str: Confirmation message with task ID and description.
    """
    deadline_dt = datetime.fromisoformat(deadline) if deadline else None
   
    task = TaskClass(
        _id=str(uuid.uuid4()),
        description=description,
        deadline=deadline_dt,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        completed=False
    )
    
    return add_to_task(task)

@tool
def get_tasks() -> list:
    """
    Retrieves all tasks from the database.
    Returns:
        list: A list of all tasks formatted as strings.
    """
    return get_all_tasks()

@tool
def get_task_by_id(task_id: str) -> str:
    """
    Retrieves a task by its ID from the database.
    
    Args:
        task_id (str): The ID of the task to retrieve.
    
    Returns:
        str: The task details or an error message if not found.
    """
    return get_task_by_id(task_id)

@tool
def delete_all_tasks() -> str:
    """
    Deletes all tasks from the database.
    
    Returns:
        str: Confirmation message indicating all tasks have been deleted.
    """
    return delete_all_tasks()

@tool
def update_task_by_id(task_id: str, description: str = None, deadline: str
                      = None, completion_status: bool = None) -> str:
    """
    Updates a task by its ID in the database.
    Args:
        task_id (str): The ID of the task to update.
        description (str, optional): The new description for the task. Defaults to None.
        deadline (str, optional): The new deadline for the task in ISO format. Defaults to None.
        completion_status (bool, optional): The new completion status for the task. Defaults to None.
    Returns:
        str: Confirmation message indicating the task has been updated or an error message if not found.
    """
    task = get_task_by_id(task_id)
    if isinstance(task, str):
        return task
    if description:
        task.update_description(description)
    if deadline:
        task.update_deadline(deadline)
    if completion_status:
        task.update_completion_status(completion_status)
    
    return update_task(task_id, task)

@tool    
def get_time() -> str:
    """
    Returns the current time in ISO format and the day of the week.
    This function can be used to get the current time for task creation or updates.
    Calculate Tomorrow, yesterday, in 'n' days, etc., using this function.
    Also calculate the day of the week.

    Returns:
        str: A string containing the current time in ISO format and the day of the week.
    """
    current_time = datetime.now()
    day_of_week = current_time.strftime("%A")  # %A gives the full weekday name (e.g., Monday)
    return f"Current time: {current_time.isoformat()}, Day: {day_of_week}"