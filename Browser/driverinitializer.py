from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import socket

class DriverInitializer:
    """Initialize driver chromedriver in various settings"""

    def __init__(self, remote_port: int = 9222):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.remote_port = remote_port
        self.driver: webdriver = None
        self.chrome_options = Options()
        self.is_using_existing_driver = False

    def start_with_existing_driver(self) -> None:
        if self.is_using_existing_driver is False:
            # Check whether port 9222 (or any if set) is occupied.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', self.remote_port))
            if result == 0:
                print("Chrome detected.")
                self.is_using_existing_driver = True
                # TODO: Set to be able to use port other than 9222
                self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            else:
                print("Chrome is not detected, instantiating new browser")
            sock.close()
        else:
            print("Cannot user existing driver when other option used.")

    # TODO - Start a driver that can be controlled with specific user directory

    def start_headless_driver(self) -> None:
        if self.is_using_existing_driver is False:
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--no-sandbox")
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            self.chrome_options.add_argument(f"--window-size=1920,1080")
        else:
            print("Creating new driver is not allowed if already using existing driver.")

    def start_with_specific_user_dir(self, user_dir: str) -> None:
        if self.is_using_existing_driver is False:
            self.chrome_options.add_argument("user-data-dir=" + user_dir)
        else:
            print("Creating new driver is not allowed if already using existing driver.")

    def get_driver(self) -> webdriver:
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        return self.driver

    @staticmethod
    def start_remote_driver() -> None:
        """Start the normal remote driver via cmd"""
        pass
        # TODO - Start remote driver (May need adiministrator privileges)

