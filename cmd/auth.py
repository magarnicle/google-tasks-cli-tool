import os
import pickle
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

def authenticate_google_tasks():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            logger.info("Refreshed existing credentials")
        else:
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
            # Suppress browser-related errors
            os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
            creds = flow.run_local_server(port=0, open_browser=False)
            logger.info("Generated new credentials")
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def logout():
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
        logger.info("User logged out successfully")
        print("You have been logged out.")
    else:
        logger.info("No user was logged in")
        print("No user is currently logged in.")
