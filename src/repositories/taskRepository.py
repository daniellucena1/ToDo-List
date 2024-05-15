from typing import List
from src.models.tasks import Task

class TaskRepository():
    tasks: List[Task]

    def __init__(self, tasks_:List[Task]) -> None:
        self.tasks = tasks_
        pass
    
    def create(self, name_:str, typ_:str) -> Task:
        task = Task(typ_, name_, len(self.tasks)+1)
        self.tasks.append(task)
        return task
    
    def delete(self, id_:int) -> bool:
        for i in range(len(self.tasks)):
            if self.tasks[i].getId() == id:
                self.tasks.remove(self.tasks[i])
                return True
        return False

    def updateTask(self, task_:Task, typ_: str) -> bool:
        for i in range(len(self.tasks)):
            if self.tasks[i].getName() == task_.getName():
                self.tasks[i].setType(typ_)
                return True
        return False
    
    def listTask(self) -> list[Task]:
        return self.tasks
    
    def getTask(self, id:int) -> Task:
        for i in range(len(self.tasks)):
            if self.tasks[i].getId() == id:
                return self.tasks[i]
        return None
    
    