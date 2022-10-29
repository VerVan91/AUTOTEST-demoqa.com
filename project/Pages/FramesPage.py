from selenium.webdriver.common.by import By
from framework.Driver.DriverUtils import DriverUtils
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Frame import Frame


class FramesPage(BaseForm):
    FRAMES_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Frames']")
    FRAMES_PAGE_NAME = "frames_page"
    UPPER_FRAME_ID = "frame1"
    LOWER_FRAME_ID = "frame2"
    UPPER_FRAME_TEXT_LOCATOR = (By.ID, "sampleHeading")
    UPPER_FRAME_TEXT_NAME = "upper_frame"
    LOWER_FRAME_TEXT_LOCATOR = (By.ID, "sampleHeading")
    LOWER_FRAME_TEXT_NAME = "lower_frame"

    def __init__(self):
        super().__init__(self.FRAMES_PAGE_LOCATOR, self.FRAMES_PAGE_NAME)
        self.upper_frame = Frame(self.UPPER_FRAME_TEXT_LOCATOR, self.UPPER_FRAME_TEXT_NAME)
        self.lower_frame = Frame(self.LOWER_FRAME_TEXT_LOCATOR, self.LOWER_FRAME_TEXT_NAME)

    def switch_to_upper_frame(self):
        DriverUtils.switch_to_frame(self.UPPER_FRAME_ID)

    def switch_to_lower_frame(self):
        DriverUtils.switch_to_frame(self.LOWER_FRAME_ID)

    def get_upper_frame_text(self):
        return self.upper_frame.get_text()

    def get_lower_frame_text(self):
        return self.lower_frame.get_text()
