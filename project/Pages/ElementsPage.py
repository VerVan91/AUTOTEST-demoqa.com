from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button


class ElementsPage(BaseForm):
    ELEMENTS_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Elements']")
    ELEMENTS_PAGE_NAME = "elements_page"
    BTN_WEB_TABLES_LOCATOR = (By.XPATH, "//*[contains(@class, 'btn-light')]//*[contains(text(), 'Web Tables')]")
    BTN_WEB_TABLES_NAME = 'btn_web_tables'

    def __init__(self):
        super().__init__(self.ELEMENTS_PAGE_LOCATOR, self.ELEMENTS_PAGE_NAME)
        self.btn_web_tables = Button(self.BTN_WEB_TABLES_LOCATOR, self.BTN_WEB_TABLES_NAME)

    def click_btn_web_tables(self):
        self.btn_web_tables.click()
