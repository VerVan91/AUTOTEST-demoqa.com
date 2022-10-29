from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name):
        if browser_name == 'chrome':
            options = ChromeOptions()
            options.add_argument('chrome')
            options.add_argument('--start-maximized')
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            return driver
        elif browser_name == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            driver.maximize_window()
            return driver
        else:
            raise ValueError(f"No such {browser_name} browser exists")
