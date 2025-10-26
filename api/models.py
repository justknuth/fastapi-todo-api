from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False
    
    
class TodoCreate(BaseModel):
    task: str
    
    
class TodoUpdate(BaseModel):
    task: Optional[str] = None
    completed: Optional[bool] = None