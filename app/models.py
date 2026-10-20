"""Domain model for a task."""
from dataclasses import dataclass


@dataclass
class Task:
    task_id: int
    title: str
    completed: bool = False

    def mark_completed(self) -> None:
        """Mark this task as completed."""
        self.completed = True
