from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Browser.gdrivepage import Locator
from Browser.gdrivepage import GdrivePageLocators as Address


class GdriveController:
    """Main class to access Google Drive's UI"""

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver.Chrome = driver
        self.driver.implicitly_wait(5)

    def get_driver(self) -> webdriver:
        return self.driver

    def validate_on_gdrive_page(self) -> None:
        """Validate if the current page is on Google Drive's UI"""
        assert self.is_element_exist(Address.DRIVE_TEXT)

    def goto_url(self, url: str) -> None:
        """Go to a specific URL"""
        self.driver.get(url)
        print("Page loaded : '" + self.driver.title + "'")

    def is_element_exist(self, locator: Locator) -> bool:
        """Check if an element exists on the current page"""
        result = self.driver.find_elements(*locator)
        if len(result) > 0:
            return True
        else:
            return False

    def set_implicit_wait(self, seconds: int = 5) -> None:
        """Set implicit wait"""
        self.driver.implicitly_wait(seconds)

    def click_element_default(self, element_locator: (str, str)) -> None:
        """Click on an element using default locator style"""
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(*element_locator)).click()

    def click_element(self, element_locator: Locator) -> None:
        """Click on an element using custom locator style"""
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element_locator)).click()
