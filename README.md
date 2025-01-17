# WinBackupPlus

WinBackupPlus is a robust backup solution for Windows systems, providing comprehensive options for backing up entire drives, system settings, and application data. This script ensures that your critical system and personal data are safely stored and easily recoverable.

## Features

- Backup entire drives, including files and folders.
- Backup Windows system settings using built-in tools.
- Backup application data from the `%APPDATA%` directory.

## Requirements

- Python 3.x
- Administrator privileges to run system backups.

## Installation

1. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine or download the script directly.

## Usage

1. Open a command prompt or terminal with administrative privileges.
2. Navigate to the directory where `win_backup_plus.py` is located.
3. Run the script with the following command:
   ```bash
   python win_backup_plus.py
   ```
4. The backup process will initiate, and logs will provide information on the progress.

## Backup Location

- The backups are saved in the `D:\Backups` directory, with each backup stored in a subdirectory named with the current date and time.

## Logging

- The script provides logging information to track the backup process. Logs include details of successful operations and any errors encountered.

## Notes

- Ensure you have enough storage space on the destination drive for the backup.
- Make sure to run the script with administrative privileges to allow access to system settings.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.