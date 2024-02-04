<p align="center"><a href="https://ideacat.ro" target="_blank"><img src="https://raw.githubusercontent.com/ideacatlab/google-tasks-cli-tool/master/.github/images/gtask.png" width="100%"></a></p>

# Google Tasks CLI Tool

This CLI tool allows you to manage your Google Tasks directly from the command line, providing a convenient way to interact with your tasks without leaving your terminal.

## Installation and Setup

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/ideacatlab/google-tasks-cli-tool.git
```

Navigate into the cloned directory and copy the `.env.example` file to `.env`:

```bash
cd google-tasks-cli-tool
cp .env.example .env
```

Fill in the `.env` file with your Google Cloud Platform credentials. Follow these steps to obtain your credentials:

1. Register for a Google Cloud Platform account if you haven't already.
2. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
3. Create a new project and enable the Google Tasks API for it.
4. Go to "Credentials", and set up your OAuth consent screen.
5. Create OAuth 2.0 Client IDs credentials and download the JSON file.
6. Extract the relevant information from the JSON file and fill it into your `.env` file accordingly.

For more details on the Google Tasks API, visit the [official documentation](https://developers.google.com/tasks?hl=en_US).

### Setting Up the `gtask` Command

To use `gtask` as a command from anywhere in your system, add an alias to your shell configuration file. For `zsh` users, edit your `.zshrc` file, and for `bash` users, edit your `.bashrc` file:

For `zsh`:

```zsh
echo 'alias gtask="python3 ~/{your_directory}/gtask/gtask.py"' >> ~/.zshrc
source ~/.zshrc
```

For `bash`:

```bash
echo 'alias gtask="python3 ~/{your_directory}/gtask/gtask.py"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

After installation and setup, you can start using the CLI tool. Here's how to use it:

```bash
gtask
```

This will launch the CLI tool, prompting you with the available commands:

```
Welcome to the Google Tasks CLI Tool!

You're logged in. Here are the available commands:
1: List non-completed tasks
0: Exit

Enter a command number:
```

To list non-completed tasks, enter `1`:

```
Task List: My Tasks (encrypted_id)

Task List: Work Projects (encrypted_id)
    ☐ Complete project proposal (encrypted_id)
    ☐ Review meeting notes (encrypted_id)

Task List: Personal (encrypted_id)
    ☐ Buy groceries (encrypted_id)
    ☐ Schedule dentist appointment (encrypted_id)

You're logged in. Here are the available commands:
1: List non-completed tasks
0: Exit

Enter a command number: 0
Exiting...
```

## Log Configuration

The Google Tasks CLI tool is configured to log important events and errors to `storage/logs/gtask.log`. The logging level and format can be adjusted in the `log.conf` file.

### Changing the Log Level

To change the log level, update the `level` under `[logger_root]` and `[handler_fileHandler]` in `log.conf`. Available log levels include:

- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

### Log Format

The log format can be customized by changing the `format` under `[formatter_fileFormatter]`. The default format includes the timestamp, logger name, log level, and message.


## Future Enhancements

- [x] OAuth Integration
- [x] List non-completed tasks
- [ ] Create new tasks
- [ ] Update existing tasks
- [ ] Delete tasks
- [ ] Set task priorities

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request. Let's make this tool even better together!

