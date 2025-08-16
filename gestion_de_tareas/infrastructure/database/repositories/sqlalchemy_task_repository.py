from typing import List, Optional, Dict
from domain.entities.task import Task
from domain.ports.task_repository_port import TaskRepositoryPort




class InMemoryTaskRepository(TaskRepositoryPort):
    
    def __init__(self):
        self._tasks: Dict[str, Task] = {}
        print(f"\nDiccionario:{self._tasks}\n")

    async def save(self, task: Task):
        self._tasks[task.id] = task
        return task

    async def get_by_id(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    async def get_all(self) -> List[Task]:
        return list(self._tasks.values())

    async def delete_by_id(self, task_id: str) -> None:
        if task_id in self._tasks:
            del self._tasks[task_id]

