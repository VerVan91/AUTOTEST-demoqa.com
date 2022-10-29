from selenium.common import TimeoutException
from framework.Driver.WebDriver import WebDriver
from framework.Utils.Logger import Logger
from framework.Utils.Waits import Waits
from selenium.webdriver.common.alert import Alert


class AlertUtils:

    @staticmethod
    def get_alert_text():
        return Alert(WebDriver.get_driver()).text

    @staticmethod
    def alert_accept():
        Alert(WebDriver.get_driver()).accept()

    @staticmethod
    def is_alert():
        try:
            Waits.get_wait_alert_is_present()
        except TimeoutException:
            Logger.log_warning("exception from func is_alert")
            return False
        return True

    @staticmethod
    def type_to_prompt(text):
        alert = WebDriver.get_driver().switch_to.alert
        alert.send_keys(text)
        alert.accept()
