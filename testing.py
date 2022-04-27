from Browser.driverinitializer import DriverInitializer
import time
import os


CURRENT_DIR = os.getcwd()

initializer = DriverInitializer()

# 1. Start with current browser
initializer.start_with_existing_driver()
# -> Able to use complex setting to be used

# 2. Start with headless browser
# initializer.start_headless_driver()


driver = initializer.get_driver()

# DriverInitializer.start_remote_driver()

driver.get("http://www.instagram.com")

time.sleep(20)
