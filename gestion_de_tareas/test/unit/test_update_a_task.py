import pytest
from unittest.mock import AsyncMock

from domain.entities.task import Task, TaskStatus
from domain.use_cases.update_a_task import UpdateTaskUseCase
from application.dtos.task_dtos import TaskResponseDTO, TaskUpdateDTO
from domain.exceptions.task_exceptions import TaskNotFoundError



@pytest.mark.asyncio
async def test_update_task_success():
    
    mock_repo = AsyncMock()
    
    mock_task_data = Task(
        name="Comprar leche",
        description="Leche entera y deslactosada",
        status=TaskStatus.PENDING
    )
    
    mock_repo.get_by_id.return_value = mock_task_data
    
    mock_dto = TaskUpdateDTO(
        name="Nuevo título",
        description="Nueva descripción"
    )
    
    use_case = UpdateTaskUseCase(task_repository=mock_repo)
    
    updated_task = await use_case.execute(task_id=mock_task_data.id, task_update_dto=mock_dto)
    
    assert isinstance(updated_task, TaskResponseDTO)
    assert updated_task.name == mock_dto.name
    assert updated_task.description == mock_dto.description
    assert updated_task.status == TaskStatus.COMPLETED
    
    mock_repo.get_by_id.assert_called_once_with(mock_task_data.id)
    mock_repo.save.assert_called_once()
    
    
@pytest.mark.asyncio
async def test_update_task_not_found():
    
    mock_repo = AsyncMock()
    
    mock_repo.get_by_id.return_value = None
    
    mock_dto = TaskUpdateDTO(
        name="Nuevo título",
        description="Nueva descripción"
    )
    
    use_case = UpdateTaskUseCase(task_repository=mock_repo)
    
    with pytest.raises(TaskNotFoundError):
        await use_case.execute(task_id="No se encontro el ID", task_update_dto=mock_dto)
    
    #Afirmar que el repositorio fue llamado una sola vez 
    mock_repo.get_by_id.assert_called_once_with("No se encontro el ID")
    # Verificamos que update NO fue llamado
    mock_repo.save.assert_not_called()
    