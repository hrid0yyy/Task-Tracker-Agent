from datetime import datetime
import uuid

class TaskClass:
    _id = str
    description: str
    deadline: datetime
    created_at: datetime
    updated_at: datetime
    completed: bool
    
    def __init__(self, _id: uuid, description: str, deadline: datetime, 
                 created_at: datetime, updated_at: datetime, completed: bool):
        self._id = str(_id) 
        self.description = description
        self.deadline = deadline
        self.created_at = created_at
        self.updated_at = updated_at
        self.completed = completed


    def update_description(self, new_description: str):
        self.description = new_description
        self.updated_at = datetime.now()
    
    def update_deadline(self, new_deadline: datetime):
        if new_deadline > datetime.now():
            self.deadline = new_deadline 
        self.updated_at = datetime.now() 
    
    def update_completion_status(self, completed: bool):
        self.completed = completed
        self.updated_at = datetime.now()
    
    def is_completed(self) -> bool:
        return self.completed


    def to_dict(self):
        return {
            "_id": self._id,
            "description": self.description,
            "deadline": self.deadline if self.deadline else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "completed": self.completed,
        }

    def __str__(self):
        return f"Task(_id={self._id}, description={self.description}, deadline={self.deadline.isoformat()}, " \
               f"created_at={self.created_at.isoformat()}, updated_at={self.updated_at.isoformat()}, completed={self.completed})"
    
    def format(self):
        return (
            f"Task ID: {self._id}\n"
            f"Description: {self.description}\n"
            f"Deadline: {self.deadline.isoformat() if self.deadline else 'No deadline'}\n"
            f"Created At: {self.created_at.isoformat()}\n"
            f"Updated At: {self.updated_at.isoformat()}\n"
            f"Completed: {'Yes' if self.completed else 'No'}\n"
        )