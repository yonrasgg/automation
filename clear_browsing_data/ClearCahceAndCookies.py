import os
import time
import psutil
import requests
import zipfile
import io
from selenium import webdriver

# ChromeDriver version and platform
chrome_version = "latest"
platform = "win64"

# Get chromedriver URL based on version and platform (win32, win64, mac64, linux64)
def get_chromedriver_url(version, platform):
    base_url = f"https://googlechromelabs.github.io/chrome-for-testing/{version}/chromedriver-{platform}.zip"
    response = requests.get(base_url)
    if response.status_code == 200:
        with open("chromedriver.zip", "wb") as zip_file:
            zip_file.write(response.content)
        with zipfile.ZipFile("chromedriver.zip", "r") as z:
            z.extractall()
        os.remove("chromedriver.zip")
    else:
        print("Unable to find the specified ChromeDriver version or platform.")


def download_and_extract_chromedriver(url):
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall()

# Define chromedriver path
chromedriver = "./chromedriver"

# Clean cookies and history
def clean_cookies_and_history():
    default_path = os.path.join(os.getcwd(), 'Cookies')  # Provide a default path if 'LOCALAPPDATA' is not set
    cookies_path = os.path.join(os.getenv('LOCALAPPDATA', default_path), 'Google', 'Chrome', 'User Data', 'Default', 'Cookies')
    history_path = os.path.join(os.getenv('LOCALAPPDATA', default_path), 'Google', 'Chrome', 'User Data', 'Default', 'History')

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

    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.google.com")
    driver.delete_all_cookies()
    driver.quit()


# Close the webdriver
if __name__ == '__main__':
    get_chromedriver_url(chrome_version, platform)
    clean_cookies_and_history()
    clean_cache()
    start_session()
    time.sleep(10)  # Wait for session to close
    clean_cookies_and_history()
    clean_cache()
    print("Cookies and cache cleaned successfully.")
    