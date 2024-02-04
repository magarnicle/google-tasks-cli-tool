import os
import logging.config
from cmd.list_tasks_cmd import list_tasks
from cmd.auth import authenticate_google_tasks

log_directory = "storage/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_config_file = 'log.conf'
if not os.path.exists(log_config_file):
    raise FileNotFoundError(f"Logging configuration file not found: {log_config_file}")

logging.config.fileConfig(fname=log_config_file, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def display_commands():
    logger.info("Displaying available commands")
    print("\nYou're logged in. Here are the available commands:")
    print("1: List non-completed tasks")
    print("0: Exit")
    return input("\nEnter a command number: ")

def main():
    logger.info("Starting the Google Tasks CLI Tool")
    print("Welcome to the Google Tasks CLI Tool!\n")
    creds = authenticate_google_tasks()
    
    while True:
        command = display_commands()
        if command == '1':
            list_tasks(creds)
        elif command == '0':
            logger.info("Exiting the tool")
            print("Exiting...")
            break
        else:
            logger.error("Invalid command entered")
            print("Invalid command.")

if __name__ == '__main__':
    main()
