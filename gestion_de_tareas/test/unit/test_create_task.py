
import pytest
from unittest.mock import AsyncMock

from domain.entities.task import Task, TaskStatus
from domain.use_cases.create_task import CreateTaskUseCase
from application.dtos.task_dtos import TaskCreateDTO, TaskResponseDTO


@pytest.mark.asyncio
async def test_create_task_use_case_success():
    
    # configurar el mock del repositorio
    mock_repo = AsyncMock()
    
    # Define el valor que el mock debe devolver cuando se llame a save
    mock_task_data = Task(
        name="Comprar leche",
        description="Leche entera y deslactosada",
        status=TaskStatus.PENDING
    )
    mock_repo.save.return_value = mock_task_data
    
    # datos de prueba
    task_create_dto = TaskCreateDTO(
        name="Comprar leche",
        description="Leche entera y deslactosada"
    )
    
    # instanciar el caso de uso con el mock
    use_case = CreateTaskUseCase(task_repository=mock_repo)
    
    # ejecutar el caso de uso
    created_task = await use_case.execute(task_create_dto=task_create_dto)
    
    # Afirmar que el repositorio se llamó correctamente
    mock_repo.save.assert_awaited_once()
    
    # Afirmar que el resultado es un TaskResponseDTO válido
    assert isinstance(created_task, TaskResponseDTO)
    assert created_task.name == task_create_dto.name
    assert created_task.description == task_create_dto.description
    assert created_task.status == TaskStatus.PENDING
    
    # afirmar que el metodo del repositorio fue llamado una vez con la tarea correcta
    mock_repo.save.assert_called_once()
    
    

