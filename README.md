# Persistent Script Setup using PowerShell on Windows

Running a script persistently means it continues running even after system reboots. This guide demonstrates setting up a persistent Python script as a Windows service using PowerShell and NSSM (Non-Sucking Service Manager).

## Pre-requisites:
- Ensure PowerShell is installed and run as an administrator.
- Have the script you wish to run persistently ready. For this guide, we'll use a Python script.

## Instructions:

### 1. Python Script Template:
The Python script below provides a basic structure for a service-like behavior. It runs continuously and can be customized to perform various tasks persistently.

```python
import time
import logging

logging.basicConfig(filename='service_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def main():
    while True:
        try:
            # Customize this block with your specific tasks
            logging.info("Service is running...")
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

### 2. Setting Up the Service using PowerShell and NSSM:
Follow these steps to set up the Python script as a Windows service:

- **Download NSSM**: Get NSSM from [here](https://nssm.cc/download) and extract `nssm.exe` to a directory.

- **PowerShell Commands**:
  ```powershell
  cd path\to\nssm
  .\nssm.exe install YourServiceName
  Start-Process -FilePath ".\nssm.exe" -ArgumentList "edit YourServiceName" -Wait
  Set-Service -Name YourServiceName -StartupType 'Automatic'
  Start-Service -Name YourServiceName
  ```

  Replace `YourServiceName` with a name for your service and configure paths accordingly.

### 3. Purpose of the Script:
This Python script template is versatile and can be adapted for various purposes, including:
- Monitoring applications or system resources.
- Automated recurring tasks.
- Real-time data processing.
- Background maintenance or automation.

The script's `main()` function serves as a placeholder for your specific tasks, allowing the script to perform any action continuously in the background.

## Notes:
- Test the script manually before setting it up as a service.
- Customize the `main()` function for your desired functionality.
- Ensure proper error handling within the script.
- Monitor system logs or implement logging within the script.
- Adjust permissions if the script interacts with sensitive operations or services.

By following these steps, you can set up your Python script to run persistently as a Windows service, catering to various continuous processing or monitoring needs.

---
### Create memory_clean.py
The `memory_clean.py` script is designed to run persistently, performing various system cleanup tasks at regular intervals. Here's a brief description of what the script does:

1. **Logging Setup:** The script sets up logging to a file named `service_log.log`, recording timestamped messages with log levels.

2. **Main Functionality Loop:** The script enters a `while True` loop, which means it will run indefinitely.

3. **System Cleanup Tasks:**
   - The script logs a message indicating that the service is running.
   - It performs various system cleanup tasks:
      - Cleans package caches using `apt-get clean` and `apt-get autoclean`.
      - Removes obsolete packages using `apt-get autoremove`.
      - Vacuums journal logs using `journalctl --vacuum-time=7d`.
      - Checks and removes old log files (use `rm -rf` with caution).
      - Cleans the cache of thumbnails.
      - Deactivates and reactivates the swap space.

4. **Simulation:** After completing the cleanup tasks, the script simulates some task by sleeping for 5 seconds. You can replace this with your actual logic or tasks.

5. **Error Handling:** If any exception occurs during the execution of cleanup tasks, it logs the error.

6. **Script Execution:** The `main` function is executed only if the script is run directly (not imported as a module).

Keep in mind that running cleanup tasks, especially removing files and logs, should be done with caution to avoid unintended data loss. Review and customize the script based on your specific needs and system configuration. Additionally, consider scheduling the script using tools like cron to execute it at specific intervals.
