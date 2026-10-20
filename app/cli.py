"""Minimal command-line interface for SecureTask."""
from app.service import TaskService


def main() -> None:
    service = TaskService()
    print("SecureTask - aplikasi pengelolaan tugas")
    print("Ketik judul tugas untuk menambahkan. Ketik 'selesai' untuk keluar.")

    while True:
        title = input("Judul tugas: ").strip()
        if title.lower() == "selesai":
            break
        try:
            task = service.create_task(title)
            print(f"Tugas #{task.task_id} berhasil ditambahkan: {task.title}")
        except ValueError as error:
            print(f"Input tidak valid: {error}")

    print("\nDaftar tugas:")
    for task in service.list_tasks():
        print(f"- [{ 'x' if task.completed else ' ' }] {task.task_id}: {task.title}")


if __name__ == "__main__":
    main()
