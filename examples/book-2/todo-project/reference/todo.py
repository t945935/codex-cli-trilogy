#!/usr/bin/env python3
"""Reference implementation for the book-2 todo workflow exercise."""
import json
import sys
from pathlib import Path

DATA = Path(__file__).with_name("todos.json")
SCHEMA_VERSION = 2


def _validate_tasks(tasks):
    if not isinstance(tasks, list):
        raise ValueError("tasks must be a JSON array")
    seen = set()
    validated = []
    for item in tasks:
        if not isinstance(item, dict):
            raise ValueError("each task must be an object")
        if set(item) != {"id", "text", "completed"}:
            raise ValueError("task object must contain only id, text, and completed")
        task_id = item.get("id")
        text = item.get("text")
        completed = item.get("completed")
        if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("task id must be a positive integer")
        if task_id in seen:
            raise ValueError("task ids must be unique")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("task text must be nonblank")
        if not isinstance(completed, bool):
            raise ValueError("completed must be true or false")
        seen.add(task_id)
        validated.append({"id": task_id, "text": text, "completed": completed})
    return validated


def _migrate_legacy(tasks):
    if not isinstance(tasks, list) or any(not isinstance(text, str) or not text.strip() for text in tasks):
        raise ValueError("legacy todo data must be an array of nonblank strings")
    return [
        {"id": task_id, "text": text, "completed": False}
        for task_id, text in enumerate(tasks, start=1)
    ]


def load_state():
    if not DATA.exists():
        return {"schema_version": SCHEMA_VERSION, "tasks": []}
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        tasks = _migrate_legacy(raw)
    elif isinstance(raw, dict) and raw.get("schema_version") == SCHEMA_VERSION:
        tasks = _validate_tasks(raw.get("tasks"))
    else:
        raise ValueError("unsupported todo data format")
    return {"schema_version": SCHEMA_VERSION, "tasks": tasks}


def save_state(state):
    DATA.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def list_tasks(tasks, open_only=False):
    visible = [task for task in tasks if not open_only or not task["completed"]]
    if not visible:
        print("No tasks found.")
        return
    for task in visible:
        marker = "x" if task["completed"] else " "
        print(f"{task['id']}. [{marker}] {task['text']}")


def main(argv):
    if not argv:
        print("Usage: python3 todo.py list [--open] | add TEXT | done ID")
        return 2
    command, *args = argv
    try:
        state = load_state()
        tasks = state["tasks"]
        if command == "list" and args in ([], ["--open"]):
            list_tasks(tasks, open_only=(args == ["--open"]))
            return 0
        if command == "add" and len(args) == 1:
            text = args[0].strip()
            if not text:
                print("Task text cannot be blank.")
                return 2
            task_id = max((task["id"] for task in tasks), default=0) + 1
            tasks.append({"id": task_id, "text": text, "completed": False})
            save_state(state)
            print(f"Added #{task_id}: {text}")
            return 0
        if command == "done" and len(args) == 1:
            try:
                task_id = int(args[0])
            except ValueError:
                print("Task ID must be an integer.")
                return 2
            task = next((item for item in tasks if item["id"] == task_id), None)
            if task is None:
                print(f"Task #{task_id} not found.")
                return 2
            if task["completed"]:
                print(f"Task #{task_id} is already complete.")
                return 0
            task["completed"] = True
            save_state(state)
            print(f"Completed #{task_id}: {task['text']}")
            return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Cannot read or save todo data: {exc}")
        return 1
    print("Usage: python3 todo.py list [--open] | add TEXT | done ID")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
