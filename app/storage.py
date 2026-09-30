import json
from pathlib import Path

from app.models import Task

DATA_FILE = Path("tasks.json")

def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return[]

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: Could not read task.json.")
        return[]

def save_tasks(tasks: list[Task]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)