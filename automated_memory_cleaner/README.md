# Automated Memory cleaner Script Setup on Ubuntu

Setting up a persistent script on Ubuntu involves creating a script that runs continuously, performing tasks at regular intervals. The provided Python script, `memory_clean.py`, is designed to run persistently on Ubuntu bash, automating various system cleanup tasks.

## Pre-requisites:
- Ensure Python is installed on your Ubuntu system.
- Familiarity with running scripts and basic system commands.

## Instructions:

### 1. Python Script Template:
The Python script below serves as a base for a persistent service on Ubuntu. It handles logging, system cleanup tasks, and provides a customizable structure for additional functionality.

```python
import time
import logging
import subprocess

# Set up logging
logging.basicConfig(filename='service_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Main functionality or tasks that need to run persistently
def main():
    while True:
        try:
            # Replace this with your specific functionality or tasks
            logging.info("Service is running...")  # Logging service activity

            # Add steps for cleaning the system
            logging.info("Cleaning the system...")

            # Clean package caches
            subprocess.run(['sudo', 'apt-get', 'clean'])
            subprocess.run(['sudo', 'apt-get', 'autoclean'])

            # Remove obsolete packages
            subprocess.run(['sudo', 'apt-get', 'autoremove'])

            # Vacuum journal logs
            subprocess.run(['sudo', 'journalctl', '--vacuum-time=7d'])

            # Check and remove old log files (use rm -rf with caution)
            subprocess.run(['sudo', 'du', '-h', '/var/log'])
            subprocess.run(['sudo', 'rm', '/var/log/*'])

            # Clean the cache of thumbnails
            subprocess.run(['rm', '-rf', '~/.cache/thumbnails'])

            # Deactivate and reactivate the swap
            subprocess.run(['sudo', 'swapoff', '-a'])
            subprocess.run(['sudo', 'swapon', '-a'])

            # Simulate some task; replace with your actual logic
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")
            # Implement proper error handling here

if __name__ == "__main__":
    main()
```

### 2. Purpose of the Script:
The `memory_clean.py` script is intended to run persistently, performing the following tasks:

- **Logging Setup:** Records timestamped messages with log levels in `service_log.log`.
- **Main Functionality Loop:** Runs continuously in a `while True` loop.
- **System Cleanup Tasks:**
   - Cleans package caches using `apt-get clean` and `apt-get autoclean`.
   - Removes obsolete packages using `apt-get autoremove`.
   - Vacuums journal logs using `journalctl --vacuum-time=7d`.
   - Checks and removes old log files (use `rm -rf` with caution).
   - Cleans the cache of thumbnails.
   - Deactivates and reactivates the swap space.
- **Simulation:** After cleanup tasks, the script simulates a task by sleeping for 5 seconds.

### 3. Execution and Customization:
- Run the script manually to test functionality before setting it up persistently.
- Customize the `main()` function for specific tasks or functionality.
- Ensure proper error handling within the script.
- Adjust permissions if interacting with sensitive operations.

By adapting and extending this script, you can create a persistent service tailored to your Ubuntu system's continuous processing or monitoring needs.

---