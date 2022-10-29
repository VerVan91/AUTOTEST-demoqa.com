from framework.Driver.BrowserFactory import BrowserFactory
from framework.Utils.DataUtils import DataUtils


class Singleton(type):
    drivers = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.drivers:
            cls.drivers[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.drivers[cls]


class WebDriver(metaclass=Singleton):

    __driver = None

    def __init__(self):
        WebDriver.__driver = BrowserFactory.get_browser(DataUtils.config_data_json()['browser_name'])

    @staticmethod
    def get_driver():
        return WebDriver.__driver

    @staticmethod
    def navigate_to(url):
        WebDriver.get_driver().get(url)

    @staticmethod
    def quit_driver():
        WebDriver.get_driver().quit()
        Singleton.drivers.pop(WebDriver)
