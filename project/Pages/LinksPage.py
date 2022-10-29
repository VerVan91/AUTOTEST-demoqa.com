from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button


class LinksPage(BaseForm):
    LINKS_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Links']")
    LINKS_PAGE_NAME = "browser_windows_page"
    BTN_HOME_LOCATOR = (By.ID, "simpleLink")
    BTN_HOME_NAME = "btn_home"

    def __init__(self):
        super().__init__(self.LINKS_PAGE_LOCATOR, self.LINKS_PAGE_NAME)
        self.btn_home = Button(self.BTN_HOME_LOCATOR, self.BTN_HOME_NAME)

    def click_btn_home(self):
        self.btn_home.click()
