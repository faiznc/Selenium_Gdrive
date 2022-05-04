import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from Browser.gdrivepage import Locator
from Browser.gdrivepage import GdrivePageLocators as Address


class GdriveController:
    """Main class to access and manipulate Google Drive's UI"""

    def __init__(self, driver: webdriver) -> None:
        self.driver: webdriver.Chrome = driver
        self.actions = ActionChains(driver)
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

    def is_any_element_visible(self, locator: Locator) -> bool:
        """Check if any element visible on the current page"""
        self.set_implicit_wait(0)
        result = self.driver.find_elements(*locator)
        self.reset_implicit_wait()
        for element in result:
            if element.is_displayed():
                return True
        return False

    def set_implicit_wait(self, seconds: int = 5) -> None:
        """Set implicit wait, default is 5 seconds"""
        self.driver.implicitly_wait(seconds)

    def reset_implicit_wait(self) -> None:
        """Reset implicit wait time to default"""
        self.driver.implicitly_wait(5)

    def click_element(self, element_locator: (str, str)) -> None:
        """Click on an element using default locator style"""
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(*element_locator)).click()

    def click_element(self, element_locator: Locator) -> None:
        """Click on an element using custom locator style"""
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element_locator)).click()

    def right_click_element(self, element_locator: Locator):
        """Right-click on an element"""
        self.right_click_element(*element_locator)

    def right_click_element(self, element_locator: (str, str)) -> None:
        """Right-click on an element"""
        element = self.driver.find_element(*element_locator)
        self.actions.context_click(element).perform()

    def upload_file(self, file_path: str) -> None:
        """Upload a file to Google Drive"""
        # For now only able to upload after manually upload a file to find the exact xpath
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        print("File uploaded : '" + file_path + "'")

    def click_visible_elements(self, element_locator: Locator, timeout: int = 5) -> None:
        """Click element(s) that only visible"""
        elements = self.driver.find_elements(*element_locator)
        for element in elements:
            if element.is_displayed():
                element.click()

    def download_file(self, file_name: str) -> None:
        """Download a file from Google Drive"""
        # Click a file with specific name
        file_locator = Locator(By.XPATH, "//div[text()='" + file_name + "']")
        self.right_click_element(file_locator)
        # Google's Animation Delay
        time.sleep(1)
        # Click the download button
        self.click_visible_elements(Address.DOWNLOAD_BTNs)
        # TODO: Re click if the right-click menu is still not open yet, and make a loop
