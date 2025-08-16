
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    
    PENDING = "pendiente"
    IN_PROGRESS = "en_progreso"
    COMPLETED = "completada"
    FAILED = "failed"
    
    
    
@dataclass
class Task:
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
    name: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now, init=False)
    updated_at: datetime = field(default_factory=datetime.now, init=False)

    def complete(self) -> None:
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()

    def update_status(self, name: str, description: str):
        self.name = name 
        self.description = description
        self.updated_at = datetime.now()


