import os
import sys
import logging.config
from cmd.list_tasks_cmd import list_tasks
from cmd.auth import authenticate_google_tasks, logout

log_directory = "storage/logs"
log_file = os.path.join(log_directory, "gtask.log")

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_config_file = "log.conf"
if not os.path.exists(log_config_file):
    raise FileNotFoundError(f"Logging configuration file not found: {log_config_file}")

logging.config.fileConfig(fname=log_config_file, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def clear_log_file():
    open(log_file, "w").close()
    logger.info("Log file cleared")


def display_commands():
    logger.info("Displaying available commands")
    print("\nYou're logged in. Here are the available commands:")
    print("1: List non-completed tasks")
    print("0: Exit")
    print("#: Logout")
    return input("\nEnter a command number: ")


def main():
    if "--clear" in sys.argv:
        clear_log_file()
        print("Log file cleared.")
        return

    logger.info("Starting the Google Tasks CLI Tool")
    # print("Welcome to the Google Tasks CLI Tool!\n")
    creds = None

    if os.path.exists("token.pickle"):
        creds = authenticate_google_tasks()
        logger.info("User already logged in")
    else:
        auth_prompt = input("Do you want to log in? Type 'Yes' or 'Y' to login: ")
        if auth_prompt.lower() in ["yes", "y"]:
            creds = authenticate_google_tasks()
        else:
            logger.info("User chose not to log in or to exit.")
            print("Exiting...")
            return

    list_tasks(creds)
    return
    while True:
        command = display_commands()
        if command == "1":
            list_tasks(creds)
        elif command == "0":
            logger.info("Exiting the tool")
            print("Exiting...")
            break
        elif command == "#":
            logout()
            creds = None
        else:
            logger.error("Invalid command entered")
            print("Invalid command.")


if __name__ == "__main__":
    main()
