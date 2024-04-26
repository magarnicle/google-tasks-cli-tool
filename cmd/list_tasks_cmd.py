import logging
from googleapiclient.discovery import build
from datetime import datetime

logger = logging.getLogger(__name__)

FORMAT = ["    ☐ ", "<title>", "(", "<id>", ")"]
FORMAT = ["☐", "<title>", "|", "<due>"]

DATE_FIELDS = [
    "completed",
    "due",
    "updated",
]


def list_tasks(creds):
    tasks = _list_tasks(creds)
    if not tasks:
        logger.info("No task lists found")
        print("No task lists found.\n")
        return
    for task in tasks:
        print(task)


def _list_tasks(creds):
    service = build("tasks", "v1", credentials=creds, cache_discovery=False)
    results = service.tasklists().list(maxResults=10).execute()
    items = results.get("items", [])

    if not items:
        logger.info("No task lists found")
        print("No task lists found.\n")
        return

    all_tasks = []
    for item in items:
        all_tasks.append(f"Task List: {item['title']} ({item['id']})")
        tasks = service.tasks().list(tasklist=item["id"], showCompleted=False).execute()
        for task in tasks.get("items", []):
            text = ""
            for token in FORMAT:
                if token.startswith("<") and token.endswith(">"):
                    field_name = token[1:-1]
                    if field_name in DATE_FIELDS:
                        value = task.get(field_name, "") or ""
                        if value:
                            text += datetime.fromisoformat(value).strftime("%Y-%m-%d")
                    else:
                        text += task.get(field_name, "") or ""
                else:
                    text += token
            all_tasks.append(text)
    return all_tasks
