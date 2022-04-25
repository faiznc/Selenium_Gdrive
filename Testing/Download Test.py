from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Instantiate headless driver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ---------- Setting path to downloaded files -------------
chrome_prefs = {"download.default_directory": r"C:\path\to\Downloads"}  # (windows)
chrome_options.experimental_options["prefs"] = chrome_prefs

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Download your file
driver.get('https://www.mockaroo.com/')
driver.find_element(By.CSS_SELECTOR,
                    "div.MuiButtonGroup-root.MuiButtonGroup-contained > button > span.MuiButton-label").click()
time.sleep(20)
