from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class DriverInitializer:

    def __init__(self, remote_port: int = 9222):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.remote_port = remote_port
        self.driver: webdriver = None
        self.chrome_options = Options()
        self.is_using_existing_driver = None
        return self.driver

    def start_with_existing_driver(self) -> webdriver:
        if self.is_using_existing_driver is None:
            self.is_using_existing_driver = True
            self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        else:
            print("Cannot user existing driver when other option used.")

        # self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        # return self.driver

    # TODO - Start a driver that can be controlled with specific user directory

    def start_headless_driver(self) -> None:
        if self.is_using_existing_driver is None:
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--no-sandbox")
            self.chrome_options.add_argument("--disable-dev-shm-usage")
        else:
            print("Creating new driver is not allowed if already using existing driver.")
        # self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        # return self.driver

    def start_with_specific_user_dir(self, user_dir: str) -> None:
        if self.is_using_existing_driver is None:
            self.chrome_options.add_argument("user-data-dir=" + user_dir)
        else:
            print("Creating new driver is not allowed if already using existing driver.")
        # self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        # return self.driver

    def start_driver(self) -> webdriver:
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        return self.driver
