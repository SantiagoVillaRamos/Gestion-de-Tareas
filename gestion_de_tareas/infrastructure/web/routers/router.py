from fastapi import APIRouter, Depends, status
from typing import List, Annotated

from infrastructure.web.dependencies import get_task_facade

from application.facade.task_facade import TasFacade

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
    facade: Annotated[TasFacade, Depends(get_task_facade)]
) -> TaskResponseDTO:
    
    return await facade.save(task_create_dto)
    
    

@router.get(
    "/get_all_tasks",
    response_model=List[TaskResponseDTO],
    summary="Obtener todas las tareas"
)
async def get_all_tasks(
    facade: Annotated[TasFacade, Depends(get_task_facade)]
) -> List[TaskResponseDTO]:
    
    return await facade.get_all()
    
        
    
@router.get(
    "/get_task/{task_id}",
    response_model=TaskResponseDTO,
    summary="Obtener una tarea por ID"
)
async def get_task_by_id(
    task_id: str,
    facade: Annotated[TasFacade, Depends(get_task_facade)]
) -> TaskResponseDTO:
    
    return await facade.get_by_id(task_id)
   
        
        
@router.delete(
    "/delete_task/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una tarea por ID"
)
async def delete_task(
    task_id: str,
    facade: Annotated[TasFacade, Depends(get_task_facade)]
):
    return await facade.delete_by_id(task_id)
    
        

@router.put(
    "/update_task/{task_id}",
    response_model=TaskResponseDTO,
    summary="Actualizar una tarea por ID"
)
async def update_task(
    task_id: str,
    task_update_dto: TaskUpdateDTO,
    facade: Annotated[TasFacade, Depends(get_task_facade)]
) -> TaskResponseDTO:
   
    return await facade.updated(task_id, task_update_dto)
    
    