"""In-memory storage for tasks."""
from app.models import Task


class TaskRepository:
    """Stores task objects in memory."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        """Create and store a task."""
        task = Task(task_id=self._next_id, title=title.strip())
        self._tasks[task.task_id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task | None:
        """Return a task or None when it does not exist."""
        return self._tasks.get(task_id)

    def list_all(self) -> list[Task]:
        """Return all tasks in insertion order."""
        return list(self._tasks.values())

    def delete(self, task_id: int) -> bool:
        """Delete a task; return whether it existed."""
        return self._tasks.pop(task_id, None) is not None
