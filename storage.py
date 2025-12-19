import json
from models import Task

FILE_PATH = "tasks.json"


def load_tasks():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2, ensure_ascii=False)

