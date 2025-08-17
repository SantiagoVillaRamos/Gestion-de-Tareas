from domain.ports.task_repository_port import TaskRepositoryPort
from infrastructure.database.repositories.sqlalchemy_task_repository import InMemoryTaskRepository  
from application.facade.task_facade import TasFacade

_global_task_repo_instance  = InMemoryTaskRepository()

def get_task_repository() -> TaskRepositoryPort:
    """
    Función de dependencia que retorna la única instancia del repositorio en memoria.
    """
    return _global_task_repo_instance 


def get_task_facade() -> TasFacade:
   return TasFacade(task_repository=get_task_repository())


