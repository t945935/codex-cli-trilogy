#!/usr/bin/env python3
"""A tiny, standard-library-only task list for learning CLI workflows."""
import json
import sys
from pathlib import Path

DATA = Path(__file__).with_name("todos.json")


def load_tasks():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text(encoding="utf-8"))


def main(argv):
    if not argv or argv[0] != "list":
        print("Usage: python3 todo.py list")
        return 2
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return 0
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
