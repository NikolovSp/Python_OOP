from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        current_task = next(t for t in self.tasks if t.name == task_name)
        if current_task is None:
            return f"Could not find task with the name {task_name}"

        current_task.completed = True
        return f"Completed task {current_task.name}"

    def clean_section(self):
        counter = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {counter} tasks."

    def view_section(self):
        task = '\n'.join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n{task}"
