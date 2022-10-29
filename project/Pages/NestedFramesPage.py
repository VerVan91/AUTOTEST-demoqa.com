from selenium.webdriver.common.by import By
from framework.Driver.DriverUtils import DriverUtils
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.Button import Button
from framework.WebElements.Frame import Frame


class NestedFramesPage(BaseForm):
    NESTED_FRAMES_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Nested Frames']")
    NESTED_FRAMES_PAGE_NAME = "nested_frames_page"
    NESTED_FRAMES_FORM_LOCATOR = (By.ID, "framesWrapper")
    NESTED_FRAMES_FORM_NAME = "nested_frames_form"
    PARENT_FRAME_ID = "frame1"
    PARENT_FRAME_LOCATOR = (By.XPATH, "//*[contains(text(), 'Parent frame')]")
    PARENT_FRAME_NAME = "parent_frame"
    CHILD_FRAME_LOCATOR = (By.XPATH, "//iframe[contains(@srcdoc,'Child')]")
    CHILD_FRAME_NAME = "child_frame"
    CHILD_FRAME_TEXT_LOCATOR = (By.XPATH, "//*[contains(text(),'Child Iframe')]")
    CHILD_FRAME_TEXT_NAME = "child_frame_text"
    BTN_FRAMES_LOCATOR = (By.XPATH, "//*[contains(@class, 'btn-light')]//*[text()= 'Frames']")
    BTN_FRAMES_NAME = "btn_frames"

    def __init__(self):
        super().__init__(self.NESTED_FRAMES_PAGE_LOCATOR, self.NESTED_FRAMES_PAGE_NAME)
        self.nested_frames_form = Frame(self.NESTED_FRAMES_FORM_LOCATOR, self.NESTED_FRAMES_FORM_NAME)
        self.parent_frame = Frame(self.PARENT_FRAME_LOCATOR, self.PARENT_FRAME_NAME)
        self.child_frame = Frame(self.CHILD_FRAME_LOCATOR, self.CHILD_FRAME_NAME)
        self.child_frame_element = Frame(self.CHILD_FRAME_TEXT_LOCATOR, self.CHILD_FRAME_TEXT_NAME)
        self.btn_frames = Button(self.BTN_FRAMES_LOCATOR, self.BTN_FRAMES_NAME)

    def switch_to_parent_frame(self):
        DriverUtils.switch_to_frame(self.PARENT_FRAME_ID)

    def switch_to_child_frame(self):
        DriverUtils.switch_to_frame(self.child_frame.get_element())

    def is_parent_frame(self):
        return self.parent_frame.get_text()

    def is_child_frame(self):
        return self.child_frame_element.get_text()

    def is_nested_frames_form(self):
        return self.nested_frames_form.is_visible_element()

    def click_btn_frames(self):
        self.btn_frames.click()
