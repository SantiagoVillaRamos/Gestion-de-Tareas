from domain.ports.task_repository_port import TaskRepositoryPort
from infrastructure.database.repositories.sqlalchemy_task_repository import InMemoryTaskRepository  


_task_repository_singleton = InMemoryTaskRepository()

def get_task_repository() -> TaskRepositoryPort:
    """
    Función de dependencia que retorna la única instancia del repositorio en memoria.
    """
    return _task_repository_singleton



