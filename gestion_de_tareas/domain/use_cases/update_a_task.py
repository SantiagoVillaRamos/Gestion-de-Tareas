
from domain.ports.task_repository_port import TaskRepositoryPort
from domain.exceptions.task_exceptions import TaskNotFoundError

from typing import Optional
from application.dtos.task_dtos import TaskResponseDTO, TaskUpdateDTO


class UpdateTaskUseCase:
    
    def __init__(self, task_repository: TaskRepositoryPort):
        self.task_repository = task_repository
        
        
    async def execute(self, task_id: str, task_update_dto:TaskUpdateDTO) -> Optional[TaskResponseDTO]:
        
        task = await self.task_repository.get_by_id(task_id)
        
        if not task:
            raise TaskNotFoundError(f"No se encontro el ID '{task_id}'")
        
        task.update_status(task_update_dto.name, task_update_dto.description)
        task.complete()
        
        await self.task_repository.updated(task, task_update_dto)
        
        return TaskResponseDTO(
            id=task.id,
            name=task.name,
            description=task.description,
            status=task.status,
            created_at=task.created_at,
            updated_at=task.updated_at
        )
    

