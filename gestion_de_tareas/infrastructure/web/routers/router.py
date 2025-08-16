from fastapi import APIRouter, Depends, status
from typing import List, Annotated

from infrastructure.web.dependencies import get_task_repository

from domain.use_cases.create_task import CreateTaskUseCase
from domain.use_cases.get_task_by_id import GetTaskByIdUseCase
from domain.use_cases.get_all_tasks import GetAllTasksUseCase
from domain.use_cases.delete_a_task import DeleteTaskUseCase
from domain.use_cases.update_a_task import UpdateTaskUseCase
from domain.ports.task_repository_port import TaskRepositoryPort

from application.dtos.task_dtos import TaskCreateDTO, TaskUpdateDTO, TaskResponseDTO


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post(
    "/created_tasks", 
    response_model=TaskResponseDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva tarea"
)
async def create_task(
    task_create_dto: TaskCreateDTO,
    repo: Annotated[TaskRepositoryPort, Depends(get_task_repository)]
) -> TaskResponseDTO:
    
    use_case = CreateTaskUseCase(task_repository=repo)
    task_entity = await use_case.execute(task_create_dto)
    return task_entity
    
    

@router.get(
    "/get_all_tasks",
    response_model=List[TaskResponseDTO],
    summary="Obtener todas las tareas"
)
async def get_all_tasks(
    repo: Annotated[TaskRepositoryPort, Depends(get_task_repository)]
) -> List[TaskResponseDTO]:
    
    use_case = GetAllTasksUseCase(task_repository=repo)
    task_entity = await use_case.execute()
    return task_entity
    
        
        
@router.get(
    "/get_task/{task_id}",
    response_model=TaskResponseDTO,
    summary="Obtener una tarea por ID"
)
async def get_task_by_id(
    task_id: str,
    repo: Annotated[TaskRepositoryPort, Depends(get_task_repository)]
) -> TaskResponseDTO:
    
    use_case = GetTaskByIdUseCase(task_repository=repo)
    task_entity = await use_case.execute(task_id)
    return task_entity
   
        
        
@router.delete(
    "/delete_task/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una tarea por ID"
)
async def delete_task(
    task_id: str,
    repo: Annotated[TaskRepositoryPort, Depends(get_task_repository)]
):
    use_case = DeleteTaskUseCase(task_repository=repo)
    await use_case.execute(task_id)
    
        

@router.put(
    "/update_task/{task_id}",
    response_model=TaskResponseDTO,
    summary="Actualizar una tarea por ID"
)
async def update_task(
    task_id: str,
    task_update_dto: TaskUpdateDTO,
    repo: Annotated[TaskRepositoryPort, Depends(get_task_repository)]
) -> TaskResponseDTO:
   
    use_case = UpdateTaskUseCase(task_repository=repo)
    task_entity = await use_case.execute(
        task_id,
        task_update_dto
    )
    return task_entity
    