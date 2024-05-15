from typing import List
from src.repositories.taskRepository import TaskRepository
from src.models.tasks import Task

class TasksController():
    repository: TaskRepository

    def __init__(self, repository_:TaskRepository) -> None:
        self.repository = repository_
        pass

    def getTask(self, id:int) -> Task:
        return self.repository.getTask(id)
    
    def create(self, name_: str, typ_: str) -> Task:
        return self.repository.create(name_, typ_)

    def delete(self, id:int) -> bool:
        return self.repository.delete(id)
    
    def update(self, task_: Task, typ_: str) -> bool:
        return self.repository.updateTask(task_, typ_)
    
    def list(self) -> List[Task]:
        return self.repository.listTask()
    