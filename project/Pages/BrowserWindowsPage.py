from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button


class BrowserWindowsPage(BaseForm):
    BROWSER_WINDOWS_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Browser Windows']")
    BROWSER_WINDOWS_PAGE_NAME = "browser_windows_page"
    BTN_NEW_TAB_LOCATOR = (By.ID, "tabButton")
    BTN_NEW_TAB_NAME = "btn_new_tab"
    BTN_ELEMENTS_LOCATOR = (By.XPATH, "//*[contains(@class, 'header-text')][text()='Elements']")
    BTN_ELEMENTS_NAME = "btn_elements"
    BTN_LINKS_LOCATOR = (By.XPATH, "//*[contains(@class, 'btn-light')]//*[text() = 'Links']")
    BTN_LINKS_NAME = "btn_links"

    def __init__(self):
        super().__init__(self.BROWSER_WINDOWS_PAGE_LOCATOR, self.BROWSER_WINDOWS_PAGE_NAME)
        self.btn_new_tab = Button(self.BTN_NEW_TAB_LOCATOR, self.BTN_NEW_TAB_NAME)
        self.btn_elements = Button(self.BTN_ELEMENTS_LOCATOR, self.BTN_ELEMENTS_NAME)
        self.btn_links = Button(self.BTN_LINKS_LOCATOR,self.BTN_LINKS_NAME)

    def click_new_tab(self):
        self.btn_new_tab.click()

    def click_btn_elements(self):
        self.btn_elements.click()

    def click_btn_links(self):
        self.btn_links.click()
