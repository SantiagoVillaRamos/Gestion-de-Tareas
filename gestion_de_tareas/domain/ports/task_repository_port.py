from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.task import Task


class TaskRepositoryPort(ABC):
    
    """Puerto de salida para el repositorio de tareas
    Define las operaciones que el repositorio de tareas debe implementar.
    """
    
    @abstractmethod
    async def save(self, task: Task) -> None:
        """Guardar una tarea en la base de datos."""
        pass

    @abstractmethod
    async def get_by_id(self, task_id: str) -> Optional[Task]:
        """Obtiene una tarea por su ID."""
        pass

    @abstractmethod
    async def get_all(self) -> List[Task]:
        """Obtiene todas las tareas."""
        pass

        
    @abstractmethod
    async def delete_by_id(self, task_id: str) -> None:
        """Elimina una tarea por su ID."""
        pass
    
    