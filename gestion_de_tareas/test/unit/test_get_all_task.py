import pytest
from unittest.mock import AsyncMock
from typing import List

from domain.entities.task import Task
from domain.use_cases.get_all_tasks import GetAllTasksUseCase
from application.dtos.task_dtos import TaskResponseDTO

@pytest.mark.asyncio
async def test_get_all_tasks_success():
    
    mock_repo = AsyncMock()
    
    mock_task_data = [
        Task(name="Tarea 1", description="Descripción 1"),
        Task(name="Tarea 2", description="Descripción 2"),
        Task(name="Tarea 3", description="Descripción 3")
    ]
    mock_repo.get_all.return_value = mock_task_data
    
    use_case = GetAllTasksUseCase(task_repository=mock_repo)
    
    tasks = await use_case.execute()
    
    assert isinstance(tasks, List)
    assert len(tasks) == 3
    assert all(isinstance(task, TaskResponseDTO) for task in tasks)
    
    mock_repo.get_all.assert_called_once()