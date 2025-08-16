from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

from domain.entities.task import TaskStatus


class TaskCreateDTO(BaseModel):
    
    name: str 
    description: Optional[str] = None
    

class TaskUpdateDTO(BaseModel):
    
    name: Optional[str] = None
    description: Optional[str] = None
    
    
class TaskResponseDTO(BaseModel):
    
    id: str
    name: str
    description: Optional[str] = None
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
        
        