from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button


class AlertsFrameWidowsPage(BaseForm):
    ALERTS_FRAME_WINDOWS_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Alerts, Frame & Windows']")
    ALERTS_FRAME_WINDOWS_PAGE_NAME = 'alerts_frame_windows_page'
    BTN_ALERTS_LOCATOR = (By.XPATH, "//*[contains(@class, 'btn-light')]//*[contains(text(), 'Alerts')]")
    BTN_ALERTS_NAME = 'btn_alerts'
    BTN_NESTED_FRAMES_LOCATOR = (By.XPATH, "//*[contains(@class, 'btn-light')]//*[contains(text(), 'Nested Frames')]")
    BTN_NESTED_FRAMES_NAME = 'btn_nested_frames'

    BTN_BROWSER_WINDOWS_LOCATOR = (By.XPATH, "//*[contains(@class, 'btn-light')]//*[contains(text(), 'Browser Windows')]")
    BTN_BROWSER_WINDOWS_NAME = 'btn_browser_windows'

    def __init__(self):
        super().__init__(self.ALERTS_FRAME_WINDOWS_PAGE_LOCATOR, self.ALERTS_FRAME_WINDOWS_PAGE_NAME)
        self.btn_alerts = Button(self.BTN_ALERTS_LOCATOR, self.BTN_ALERTS_NAME)
        self.btn_nested_frames = Button(self.BTN_NESTED_FRAMES_LOCATOR, self.BTN_NESTED_FRAMES_NAME)
        self.btn_browser_windows = Button(self.BTN_BROWSER_WINDOWS_LOCATOR, self.BTN_BROWSER_WINDOWS_NAME)

    def click_btn_alerts(self):
        self.btn_alerts.click()

    def click_btn_nested_frames(self):
        self.btn_nested_frames.click()

    def click_btn_browser_windows(self):
        self.btn_browser_windows.click()
