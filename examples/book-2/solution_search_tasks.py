"""Reference repair for the search exercise."""

TASKS = ["Review API design", "Write release notes", "Test api client"]


def _normalize(text):
    return text.casefold()


def search(query, tasks=TASKS):
    if not query:
        return []
    needle = _normalize(query)
    return [task for task in tasks if needle in _normalize(task)]
