import os
import shutil
import subprocess
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_drives():
    """Get all the available drives in the system."""
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in range(26):
        if bitmask & 1:
            drives.append(chr(65 + letter) + ":\\")
        bitmask >>= 1
    return drives


def backup_drive(drive, destination):
    """Backup an entire drive to the destination."""
    try:
        if not os.path.isdir(destination):
            os.makedirs(destination)
        logging.info(f"Backing up {drive} to {destination}")
        shutil.copytree(drive, destination, dirs_exist_ok=True)
    except Exception as e:
        logging.error(f"Error backing up drive {drive}: {e}")


def backup_system_settings(destination):
    """Backup system settings using Windows built-in tools."""
    try:
        logging.info("Backing up system settings")
        system_backup_command = f"wbadmin start systemstatebackup -backupTarget:{destination}"
        subprocess.run(system_backup_command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error backing up system settings: {e}")


def backup_application_data(source, destination):
    """Backup application data."""
    try:
        logging.info(f"Backing up application data from {source} to {destination}")
        if not os.path.isdir(destination):
            os.makedirs(destination)
        shutil.copytree(source, destination, dirs_exist_ok=True)
    except Exception as e:
        logging.error(f"Error backing up application data: {e}")


def main():
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_root = f"D:\\Backups\\{current_time}"

    drives = get_drives()
    for drive in drives:
        backup_destination = os.path.join(backup_root, drive.strip(":\\"))
        backup_drive(drive, backup_destination)

    system_settings_destination = os.path.join(backup_root, "SystemSettings")
    backup_system_settings(system_settings_destination)

    application_data_source = os.path.expandvars(r"%APPDATA%")
    application_data_destination = os.path.join(backup_root, "ApplicationData")
    backup_application_data(application_data_source, application_data_destination)

    logging.info("Backup completed successfully")


if __name__ == "__main__":
    main()