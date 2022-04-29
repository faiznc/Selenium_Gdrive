from selenium import webdriver

from Browser.driverinitializer import DriverInitializer
import Browser.gdrivecontroller as gdrive
from Browser.gdrivepage import GdrivePageLocators as Address

initializer = DriverInitializer()
driver: webdriver = None

URL = "https://drive.google.com/drive/folders/134nycFTxRcz6F4gj60nHbaOEuMmDjUvc?usp=sharing"


def start_with_existing_driver():
    """Start with current browser"""
    global driver
    initializer.start_with_existing_driver()
    driver = initializer.get_driver()


if __name__ == '__main__':
    # Need to start with existing driver to access Google Drive upload functionality
    start_with_existing_driver()
    gd = gdrive.GdriveController(driver)
    gd.goto_url(URL)
    gd.validate_on_gdrive_page()
    gd.click_element(Address.ITEM1)

    gd.upload_file("D:\Faiz\Projects\Selenium_Gdrive\.gitignore")

