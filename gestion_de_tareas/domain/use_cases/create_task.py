from domain.entities.task import Task   
from domain.ports.task_repository_port import TaskRepositoryPort

from application.dtos.task_dtos import TaskResponseDTO, TaskCreateDTO
from typing import Optional


class CreateTaskUseCase:
    
    def __init__(self, task_repository: TaskRepositoryPort):
        self.task_repository = task_repository
        
    async def execute(self, task_create_dto: TaskCreateDTO) -> Optional[TaskResponseDTO]:
        
        new_task = Task(
            name=task_create_dto.name,
            description=task_create_dto.description,
        )
        
        await self.task_repository.save(new_task)
        
        return TaskResponseDTO(
            id=new_task.id,
            name=new_task.name,
            description=new_task.description,
            status=new_task.status,
            created_at=new_task.created_at,
            updated_at=new_task.updated_at
        )
    
    
