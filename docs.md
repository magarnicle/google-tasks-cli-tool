# Google Tasks API Integration in Python

This documentation provides a technical guide to integrating Google Tasks with Python applications, emphasizing command-line interactions for task management. It covers OAuth 2.0 setup, necessary libraries, and basic CRUD operations for tasks.

## Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Authentication Setup](#authentication-setup)
  - [OAuth 2.0 Details](#oauth-20-details)
  - [Secure Credential Storage](#secure-credential-storage)
- [Google API Client Library Installation](#google-api-client-library-installation)
- [User Authentication Process](#user-authentication-process)
- [Task Operations](#task-operations)
  - [Task Creation](#task-creation)
  - [Task Listing](#task-listing)
  - [Task Deletion](#task-deletion)
- [CLI Tool Development](#cli-tool-development)
  - [OAuth Integration](#oauth-integration)
  - [Command Implementation](#command-implementation)
- [Error Handling](#error-handling)

## Introduction

Integrating Google Tasks via its API allows developers to extend task management capabilities into Python applications, facilitating operations like creating, listing, and deleting tasks.

## Prerequisites

- Google Cloud Platform account with the Tasks API enabled.
- Python 3.7+.
- A secure method to store and access Google API credentials.

## Authentication Setup

### OAuth 2.0 Details

OAuth 2.0 is required for user authentication. Set up OAuth credentials in the Google Developers Console, which provides a JSON object similar to:

```json
{
  "installed": {
    "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    ...
  }
}
```

### Secure Credential Storage

Use environment variables or encrypted storage to keep OAuth credentials safe. Avoid hardcoding them in your application.

## Google API Client Library Installation

```bash
pip install google-api-python-client
```

This library simplifies making requests to the Google Tasks API.

## User Authentication Process

Use the `InstalledAppFlow` class for handling OAuth 2.0 flow:

```python
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/tasks']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file('path/to/credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds
```

### Task Operations

#### Task Creation

To create a task within a specific task list, use the `tasks.insert` method along with the ID of the task list. For creating subtasks, include the parent task's ID in the request body.

**Python Example:**

```python
def create_task(service, tasklist_id, title, parent_id=None):
    task = {'title': title}
    if parent_id:
        task['parent'] = parent_id
    result = service.tasks().insert(tasklist=tasklist_id, body=task).execute()
    print(f"Task created: {result['title']} (ID: {result['id']})")
```

**HTTP Request Example:**

```
POST https://www.googleapis.com/tasks/v1/lists/{tasklist_id}/tasks
Content-Type: application/json

{
  "title": "New Task",
  "parent": "parent_task_id"  // Optional for subtasks
}
```

#### Task Listing

To retrieve tasks from a task list, use the `tasks.list` method. You can include optional parameters like `showCompleted=false` to filter the returned tasks.

**Python Example:**

```python
def list_tasks(service, tasklist_id):
    tasks = service.tasks().list(tasklist=tasklist_id, showCompleted=False).execute()
    for task in tasks.get('items', []):
        print(f"{task['title']} (ID: {task['id']})")
```

**HTTP Request Example:**

```
GET https://www.googleapis.com/tasks/v1/lists/{tasklist_id}/tasks?showCompleted=false
```

#### Task Deletion

To delete a task, use the `tasks.delete` method with the task's unique ID and the ID of the task list it belongs to.

**Python Example:**

```python
def delete_task(service, tasklist_id, task_id):
    service.tasks().delete(tasklist=tasklist_id, task=task_id).execute()
    print(f"Task {task_id} deleted.")
```

**HTTP Request Example:**

```
DELETE https://www.googleapis.com/tasks/v1/lists/{tasklist_id}/tasks/{task_id}
```

### CLI Tool Development

Build a command-line interface (CLI) for task management using Python's `argparse` library. This allows users to interact with Google Tasks directly from the terminal.

**Python Example:**

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Google Tasks CLI Tool')
    parser.add_argument('--list', help='List all tasks', action='store_true')
    parser.add_argument('--create', help='Create a new task', type=str)
    parser.add_argument('--delete', help='Delete a task by ID', type=str)
    args = parser.parse_args()

    # Initialize Google Tasks service
    service = authenticate_google_tasks()

    if args.list:
        list_tasks(service, 'your_tasklist_id')
    elif args.create:
        create_task(service, 'your_tasklist_id', args.create)
    elif args.delete:
        delete_task(service, 'your_tasklist_id', args.delete)

if __name__ == '__main__':
    main()
```

### OAuth Integration

On the first use, prompt users to authenticate via a generated URL. Securely store the OAuth access tokens for making authenticated requests in subsequent uses.

**Python Example:**

```python
from google_auth_oauthlib.flow import InstalledAppFlow

def authenticate_google_tasks():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    # Store credentials for future use
    return creds
```

### Command Implementation

Map each CLI command to a specific function that implements the corresponding task operation (e.g., create, list, delete).

### Error Handling

Incorporate robust error handling to manage API errors, connectivity issues, and rate limits. Implement retry mechanisms, preferably with exponential backoff, for transient errors.

**Python Example:**

```python
import time

def robust_request(callable, *args, **kwargs):
    for retry in range(MAX_RETRIES):
        try:
            return callable(*args, **kwargs)
        except Exception as e:
            print(f"Request failed: {e}. Retrying in {2 ** retry} seconds.")
            time.sleep(2 ** retry)
    print("Max retries exceeded.")
```

This concise guide focuses on the technical aspects of leveraging the Google Tasks API for task manipulation through Python. For comprehensive details on the API's capabilities, refer to the official [Google Tasks API documentation](https://developers.google.com/tasks).