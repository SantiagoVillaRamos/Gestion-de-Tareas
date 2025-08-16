import pytest
from unittest.mock import AsyncMock

from domain.entities.task import Task
from domain.use_cases.delete_a_task import DeleteTaskUseCase
from domain.exceptions.task_exceptions import TaskNotFoundError


@pytest.mark.asyncio
async def test_delete_a_task_success():
    
    mock_repo = AsyncMock()
    
    mock_task_data = Task(
        name="Comprar leche",
        description="Leche entera y deslactosada",
    )
    
    mock_repo.get_by_id.return_value = mock_task_data
    
    use_case = DeleteTaskUseCase(task_repository=mock_repo)
    
    await use_case.execute(task_id=mock_task_data.id)

    mock_repo.get_by_id.assert_called_once_with(mock_task_data.id)
    mock_repo.delete_by_id.assert_called_once_with(mock_task_data.id)


@pytest.mark.asyncio
async def test_delete_task_not_found():
    
    mock_repo = AsyncMock()
    
    mock_repo.get_by_id.return_value = None
    
    use_case = DeleteTaskUseCase(task_repository=mock_repo)
    
    with pytest.raises(TaskNotFoundError):
        await use_case.execute(task_id="No se encontro el ID")

    mock_repo.get_by_id.assert_called_once_with("No se encontro el ID")
    mock_repo.delete_by_id.assert_not_called()
    