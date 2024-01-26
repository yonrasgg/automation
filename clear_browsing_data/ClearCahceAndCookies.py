import os
import time
import psutil
from getpass import getpass
from selenium import webdriver
import psutil
from selenium import webdriver

# ChromeDriver path
chromedriver = f'\\ClearCahceAndCookies\\chromedriver.exe'


# Clean cookies and history
def clean_cookies_and_history():
    cookies_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'Cookies')
    history_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'History')
    for path, name in [(cookies_path, "Cookies"), (history_path, "History")]:
        if os.path.isfile(path):
            os.remove(path)
        else:
            print(f"The file {path} does not exist.")
    print(f"{name} cleaned.")


# Clean chrome cache
def clean_cache():
    for process in psutil.process_iter(['pid', 'name']):
        if 'chrome.exe' in process.info['name'].lower():
            try:
                process.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    print("Cache cleaned.")


# Start session
def start_session():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)# Use executable_path keyword argument
    driver.get("https://www.google.com")
    driver.delete_all_cookies()
    driver.quit()


# Close the webdriver
if __name__ == '__main__':
    clean_cookies_and_history()
    clean_cache()
    start_session()
    time.sleep(10)# Wait for session to close
    clean_cookies_and_history()
    clean_cache()
    print("Cookies and cache cleaned successfully.")
