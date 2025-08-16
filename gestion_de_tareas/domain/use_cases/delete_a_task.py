from domain.ports.task_repository_port import TaskRepositoryPort
from domain.exceptions.task_exceptions import TaskNotFoundError


class DeleteTaskUseCase:
    
    def __init__(self, task_repository: TaskRepositoryPort):
        self.task_repository = task_repository
        
    async def execute(self, task_id: str) -> None:
        
        tasks_id = await self.task_repository.get_by_id(task_id)
        
        if not tasks_id:
            raise TaskNotFoundError(f"No se encontro el ID '{task_id}'")
        
        await self.task_repository.delete_by_id(task_id)
    
        