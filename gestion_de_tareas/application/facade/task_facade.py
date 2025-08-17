
from domain.use_cases.create_task import CreateTaskUseCase
from domain.use_cases.delete_a_task import DeleteTaskUseCase
from domain.use_cases.get_all_tasks import GetAllTasksUseCase
from domain.use_cases.get_task_by_id import GetTaskByIdUseCase
from domain.use_cases.update_a_task import UpdateTaskUseCase
from domain.ports.task_repository_port import TaskRepositoryPort
from application.dtos.task_dtos import (TaskCreateDTO, TaskResponseDTO, TaskUpdateDTO)

from typing import Optional, List


class TasFacade:
    
    def __init__(self, task_repository: TaskRepositoryPort):
        
        self.created_task_use_case = CreateTaskUseCase(task_repository)
        self.updated_task_use_case = UpdateTaskUseCase(task_repository)
        self.delete_task_use_case = DeleteTaskUseCase(task_repository)
        self.get_all_task_use_case = GetAllTasksUseCase(task_repository)
        self.get_task_by_use_case = GetTaskByIdUseCase(task_repository)
        
    async def save(self, task_create_dto: TaskCreateDTO) -> Optional[TaskResponseDTO]:
        return await self.created_task_use_case.execute(task_create_dto)
    
    async def updated(self, task_id: str, task_update_dto:TaskUpdateDTO) -> Optional[TaskResponseDTO]:
        return await self.updated_task_use_case.execute(task_id, task_update_dto)
    
    async def delete_by_id(self, task_id: str) -> None:
        await self.delete_task_use_case.execute(task_id)
    
    async def get_all(self)-> Optional[List[TaskResponseDTO]]:
        return await self.get_all_task_use_case.execute()
    
    async def get_by_id(self, task_id: str) -> Optional[TaskResponseDTO]:
        return await self.get_task_by_use_case.execute(task_id)


