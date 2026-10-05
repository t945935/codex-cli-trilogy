"""Search small task records; one behavior is intentionally incorrect."""

TASKS = ["Review API design", "Write release notes", "Test api client"]


def search(query, tasks=TASKS):
    if not query:
        return []
    # Intentional bug: requirement is case-insensitive search.
    return [task for task in tasks if query in task]
