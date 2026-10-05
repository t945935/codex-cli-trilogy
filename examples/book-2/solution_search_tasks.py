"""Reference repair for the search exercise."""

TASKS = ["Review API design", "Write release notes", "Test api client"]


def search(query, tasks=TASKS):
    if not query:
        return []
    needle = query.casefold()
    return [task for task in tasks if needle in task.casefold()]
