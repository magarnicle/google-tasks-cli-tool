import logging
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

def list_tasks(creds):
    service = build('tasks', 'v1', credentials=creds, cache_discovery=False)
    results = service.tasklists().list(maxResults=10).execute()
    items = results.get('items', [])
    
    if not items:
        logger.info("No task lists found")
        print('\nNo task lists found.\n')
        return

    for item in items:
        print(f"\nTask List: {item['title']} ({item['id']})")
        tasks = service.tasks().list(tasklist=item['id'], showCompleted=False).execute()
        for task in tasks.get('items', []):
            print(f"    ☐ {task['title']} ({task.get('id')})")
