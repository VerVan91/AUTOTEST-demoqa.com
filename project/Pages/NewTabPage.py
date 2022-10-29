from selenium.webdriver.common.by import By
from framework.Pages.BaseForm import BaseForm


class NewTabPage(BaseForm):
    NEW_TAB_PAGE_LOCATOR = (By.ID, "sampleHeading")
    NEW_TAB_PAGE_NAME = "new_tab_page"

    def __init__(self):
        super().__init__(self.NEW_TAB_PAGE_LOCATOR, self.NEW_TAB_PAGE_NAME)
