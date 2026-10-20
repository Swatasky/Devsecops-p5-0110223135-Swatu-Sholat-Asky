"""Unit tests for SecureTask business rules."""
import pytest

from app.service import TaskService


def test_create_task_trims_title() -> None:
    service = TaskService()
    task = service.create_task("  Belajar DevSecOps  ")
    assert task.title == "Belajar DevSecOps"
    assert task.task_id == 1


def test_create_task_rejects_empty_title() -> None:
    service = TaskService()
    with pytest.raises(ValueError):
        service.create_task("   ")


def test_complete_task_changes_status() -> None:
    service = TaskService()
    task = service.create_task("Menulis laporan")
    completed = service.complete_task(task.task_id)
    assert completed.completed is True


def test_complete_missing_task_raises_error() -> None:
    service = TaskService()
    with pytest.raises(LookupError):
        service.complete_task(99)


def test_delete_task() -> None:
    service = TaskService()
    task = service.create_task("Tugas contoh")
    assert service.delete_task(task.task_id) is True
    assert service.list_tasks() == []
