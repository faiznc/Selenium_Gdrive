from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

URL: str = "https://drive.google.com/drive/folders/134nycFTxRcz6F4gj60nHbaOEuMmDjUvc?usp=sharing"

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ---------- Setting path to downloaded files -------------
chrome_prefs = {"download.default_directory": r"C:\path\to\Downloads"}  # (windows)
chrome_options.experimental_options["prefs"] = chrome_prefs

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Download your file
driver.get(URL)

# SetTargetElement
targetFile = (By.XPATH, '//*[text()="MOCK_DATA.csv"]')

# driver.find_element(By.XPATH, "//*[text()='MOCK_DATA.csv']").click()

driver.find_element(*targetFile).click()
time.sleep(2)
driver.find_element(*targetFile).click()
time.sleep(20)
