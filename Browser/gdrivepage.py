from selenium.webdriver.common.by import By


class Locator:
    """A class to represent a locator that used to find an element on the page"""
    def __init__(self, by: By, value: str):
        self.data: tuple[By, str] = (by, value)

    def __iter__(self):
        return self.data.__iter__()


class GdrivePageLocators:
    """A class for Google Drive locators. All locator should come from here """

    DRIVE_TEXT = Locator(By.CSS_SELECTOR, "span.gb_5d.gb_2c")
    ITEM1 = Locator(By.CSS_SELECTOR, "c-wiz > c-wiz > div > c-wiz:nth-child(1) > div > div")
    DOWNLOAD_BTNs = Locator(By.XPATH, "//div/span[2]/span/div[@data-tooltip='Download']")
