from typing import List, Optional
from domain.ports.task_repository_port import TaskRepositoryPort

from application.dtos.task_dtos import TaskResponseDTO



class GetAllTasksUseCase:
    
    def __init__(self, task_repository: TaskRepositoryPort):
        self.task_repository = task_repository
        
    async def execute(self) -> Optional[List[TaskResponseDTO]]:
        
        tasks = await self.task_repository.get_all()
        if not tasks:
            return []
        
        return [
            TaskResponseDTO(
                id=task.id,
                name=task.name,
                description=task.description,
                status=task.status,
                created_at=task.created_at,
                updated_at=task.updated_at
            ) for task in tasks
        ]