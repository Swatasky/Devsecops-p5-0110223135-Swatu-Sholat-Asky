"""Business rules for task operations."""
from app.models import Task
from app.repository import TaskRepository
from app.validators import normalize_title


class TaskService:
    """Validates input and coordinates task operations."""

    def __init__(self, repository: TaskRepository | None = None) -> None:
        self.repository = repository or TaskRepository()

    def create_task(self, title: str) -> Task:
        """Create a task after validating its title."""
        validated_title = normalize_title(title)
        return self.repository.add(validated_title)

    def complete_task(self, task_id: int) -> Task:
        """Mark an existing task as completed."""
        task = self.repository.get(task_id)
        if task is None:
            raise LookupError("Tugas tidak ditemukan.")
        task.mark_completed()
        return task

    def list_tasks(self) -> list[Task]:
        """List all tasks."""
        return self.repository.list_all()

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its identifier."""
        return self.repository.delete(task_id)
