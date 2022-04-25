from Browser.driverController import DriverInitializer
import time


driver = DriverInitializer()
driver.start_with_existing_driver()
driver = driver.start_driver()

driver.get("http://www.google.com")
time.sleep(20)
