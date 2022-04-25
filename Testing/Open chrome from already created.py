from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#
import time
## Use current browser.
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service(executable_path=ChromeDriverManager().install(), port=9223)
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("http://www.google.com")
time.sleep(10)