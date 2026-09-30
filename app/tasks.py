from app.models import Task
from app.storage import load_tasks, save_tasks

tasks: list[Task] = load_tasks()

def add_task(title: str) -> Task:

    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    # Use max existing ID + 1 to avoid duplicate IDs if tasks are deleted
    next_id = max((t["id"] for t in tasks), default=0) + 1

    task: Task = {
        # "id": len(tasks) + 1,
        "id": next_id,
        "title": title,
        "completed": False,
    }

    tasks.append(task)

    save_tasks(tasks)

    return task

def get_tasks() -> list[Task]:  

    if not tasks:
        print("No task yet.")
        return tasks
    
    for task in tasks:
        status = "✓" if task["completed"] else " "

        print(f"{task['id']}. [{status}] {task['title']}")
    
    return tasks

def complete_task(task_id: int) -> Task:

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True

            save_tasks(tasks)

            return task

    raise ValueError("Task not found.")

def delete_task(task_id: int) -> Task:

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            save_tasks(tasks)

            return task

    raise ValueError("Task not found.")
