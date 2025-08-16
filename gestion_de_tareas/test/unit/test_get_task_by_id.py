import pytest
from unittest.mock import AsyncMock

from domain.entities.task import Task
from domain.use_cases.get_task_by_id import GetTaskByIdUseCase
from application.dtos.task_dtos import TaskResponseDTO
from domain.exceptions.task_exceptions import TaskNotFoundError


@pytest.mark.asyncio
async def test_get_by_id_tasks_success():
    
    mock_repo = AsyncMock()
    
    mock_task_data = Task(
        name="Comprar leche",
        description="Leche entera y deslactosada",
    )
    
    mock_repo.get_by_id.return_value = mock_task_data
    
    use_case = GetTaskByIdUseCase(task_repository=mock_repo)
    
    tasks = await use_case.execute(task_id=mock_task_data.id)
    
    assert isinstance(tasks, TaskResponseDTO)
    assert tasks.id == mock_task_data.id
    assert tasks.description == mock_task_data.description
    
    mock_repo.get_by_id.assert_called_once()
    
    
    
@pytest.mark.asyncio
async def test_get_task_by_id_not_found():
    
    mock_repo = AsyncMock()
    
    mock_repo.get_by_id.return_value = None
    
    use_case = GetTaskByIdUseCase(task_repository=mock_repo)
    
    with pytest.raises(TaskNotFoundError):
        await use_case.execute(task_id="No se encontro el ID")
    
    mock_repo.get_by_id.assert_called_once()