#!/usr/bin/env python3
"""Reference solution for the book-1 add/list exercise."""
import json
import sys
from pathlib import Path

DATA = Path(__file__).with_name("todos.json")


def load_tasks():
    if not DATA.exists():
        return []
    tasks = json.loads(DATA.read_text(encoding="utf-8"))
    if not isinstance(tasks, list) or any(not isinstance(item, str) for item in tasks):
        raise ValueError("Todo data must be a JSON array of strings.")
    return tasks


def save_tasks(tasks):
    DATA.write_text(json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv):
    if not argv:
        print("Usage: python3 todo.py list | add TEXT")
        return 2
    command, *args = argv
    try:
        tasks = load_tasks()
        if command == "list" and not args:
            if not tasks:
                print("No tasks yet.")
            for index, text in enumerate(tasks, start=1):
                print(f"{index}. {text}")
            return 0
        if command == "add" and len(args) == 1:
            text = args[0].strip()
            if not text:
                print("Task text cannot be blank.")
                return 2
            tasks.append(text)
            save_tasks(tasks)
            print("Added: " + text)
            return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Cannot read or save todo data: {exc}")
        return 1
    print("Usage: python3 todo.py list | add TEXT")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
