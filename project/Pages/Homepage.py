from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button


class Homepage(BaseForm):
    HOMEPAGE_LOCATOR = (By.XPATH, "//*[@class='home-body']")
    HOMEPAGE_NAME = 'homepage'
    BTN_ALERTS_FRAMES_WINDOWS_PAGE_LOCATOR = (By.XPATH, "//*[text() = 'Alerts, Frame & Windows']")
    BTN_ALERTS_FRAMES_WINDOWS_PAGE_NAME = 'homepage_btn_to_alerts_frames_windows'
    BTN_ELEMENTS_PAGE_LOCATOR = (By.XPATH, "//*[text() = 'Elements']")
    BTN_ELEMENTS_PAGE_NAME = 'homepage_btn_to_elements'

    def __init__(self):
        super().__init__(self.HOMEPAGE_LOCATOR, self.HOMEPAGE_NAME)
        self.btn_homepage_alerts = Button(self.BTN_ALERTS_FRAMES_WINDOWS_PAGE_LOCATOR,
                                          self.BTN_ALERTS_FRAMES_WINDOWS_PAGE_NAME)
        self.btn_homepage_elements = Button(self.BTN_ELEMENTS_PAGE_LOCATOR, self.BTN_ELEMENTS_PAGE_NAME)

    def open_alerts_frame_windows(self):
        self.btn_homepage_alerts.click()

    def open_elements(self):
        self.btn_homepage_elements.click()
