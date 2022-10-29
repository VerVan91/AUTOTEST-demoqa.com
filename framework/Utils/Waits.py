from framework.Driver.WebDriver import WebDriver
from framework.Utils.DataUtils import DataUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:
    WAIT_TIME = DataUtils.config_data_json()['wait_time']
    ALERT_WAIT_TIME = DataUtils.config_data_json()['alert_wait_time']

    @staticmethod
    def get_wait_all_visibility(by_locator):
        return WebDriverWait(WebDriver.get_driver(), Waits.WAIT_TIME).until(EC.visibility_of_all_elements_located(by_locator))

    @staticmethod
    def get_wait_alert_is_present():
        return WebDriverWait(WebDriver.get_driver(), Waits.ALERT_WAIT_TIME).until(EC.alert_is_present())

    @staticmethod
    def get_wait_one_visibility(by_locator):
        return WebDriverWait(WebDriver.get_driver(), Waits.WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
