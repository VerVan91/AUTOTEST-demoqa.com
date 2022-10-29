import pytest
from framework.Driver.WebDriver import WebDriver
from framework.Utils.DataUtils import DataUtils


@pytest.fixture
def setup():
    WebDriver()
    WebDriver.get_driver()
    WebDriver.navigate_to(DataUtils.config_data_json()['url'])
    yield
    WebDriver.quit_driver()
