from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button
from framework.WebElements.Text import Text


class AlertsPage(BaseForm):
    ALERTS_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Alerts']")
    ALERTS_PAGE_NAME = 'alerts_page'
    BTN_TO_SEE_ALERT_LOCATOR = (By.ID, "alertButton")
    BTN_TO_SEE_ALERT_NAME = "btn_to_see_alert"
    BTN_TO_CONFIRM_LOCATOR = (By.ID, "confirmButton")
    BTN_TO_CONFIRM_NAME = "btn_to_confirm"
    RESULT_OF_CONFIRM_LOCATOR = (By.ID, "confirmResult")
    RESULT_OF_CONFIRM_NAME = "result_of_confirm"
    BTN_TO_PROMPT_LOCATOR = (By.ID, "promtButton")
    BTN_TO_PROMPT_NAME = "btn_to_prompt"
    RESULT_OF_PROMPT_LOCATOR = (By.ID, "promptResult")
    RESULT_OF_PROMPT_NAME = "result_of_prompt"
    ALERTS_FRAME_WINDOWS_TITLE_NAME = "alerts_frame_windows_title"

    def __init__(self):
        super().__init__(self.ALERTS_PAGE_LOCATOR, self.ALERTS_PAGE_NAME)
        self.btn_to_see_alert = Button(self.BTN_TO_SEE_ALERT_LOCATOR, self.BTN_TO_SEE_ALERT_NAME)
        self.btn_to_confirm = Button(self.BTN_TO_CONFIRM_LOCATOR, self.BTN_TO_CONFIRM_NAME)
        self.result_of_confirm = Text(self.RESULT_OF_CONFIRM_LOCATOR, self.RESULT_OF_CONFIRM_NAME)
        self.btn_to_prompt = Button(self.BTN_TO_PROMPT_LOCATOR, self.BTN_TO_PROMPT_NAME)
        self.result_of_prompt = Text(self.RESULT_OF_PROMPT_LOCATOR, self.RESULT_OF_PROMPT_NAME)

    def click_btn_to_see_alert(self):
        self.btn_to_see_alert.click()

    def click_btn_to_confirm(self):
        self.btn_to_confirm.click()

    def result_confirm_text(self):
        return self.result_of_confirm.get_text()

    def click_btn_to_prompt(self):
        self.btn_to_prompt.click()

    def result_prompt_text(self):
        full_text = self.result_of_prompt.get_text()
        text = full_text[12:]
        return text
