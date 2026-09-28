from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel
class Priority(str,Enum):
    LOW="low"
    MEDIUM="medium"
    HIGH="high"



class Task(BaseModel):
    id: int 
    title: str
    completed: bool
    priority:Priority