import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from cmd.list_tasks_cmd import list_tasks
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

def authenticate_google_tasks():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use environment variables to create OAuth2 credentials
            client_config = {
                "installed": {
                    "client_id": os.getenv("CLIENT_ID"),
                    "project_id": os.getenv("PROJECT_ID"),
                    "auth_uri": os.getenv("AUTH_URI"),
                    "token_uri": os.getenv("TOKEN_URI"),
                    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
                    "client_secret": os.getenv("CLIENT_SECRET"),
                    "redirect_uris": [os.getenv("REDIRECT_URIS")]
                }
            }
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def display_commands():
    print("\nYou're logged in. Here are the available commands:")
    print("1: List non-completed tasks")
    print("0: Exit")
    return input("\nEnter a command number: ")

def main():
    print("Welcome to the Google Tasks CLI Tool!\n")
    creds = None
    if not os.path.exists('token.pickle'):
        auth_prompt = input("You need to be logged in to use this tool. Type 'Yes' or 'Y' to login: ")
        if auth_prompt.lower() not in ['yes', 'y']:
            print("Authentication required to use this tool.")
            return
        creds = authenticate_google_tasks()
    else:
        creds = authenticate_google_tasks()
    
    while True:
        command = display_commands()
        if command == '1':
            list_tasks(creds)
        elif command == '0':
            print("Exiting...")
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()
