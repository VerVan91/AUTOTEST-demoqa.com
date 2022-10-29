from framework.Utils.Logger import Logger
from framework.Utils.Waits import Waits


class BaseElement:

    def __init__(self, by_locator, name):
        self.by_locator = by_locator
        self.name = name
        Logger.log_info(f"{self.name} is active")

    def click(self):
        Waits.get_wait_one_visibility(self.by_locator).click()

    def is_visible_element(self):
        elements = Waits.get_wait_all_visibility(self.by_locator)
        return bool(elements)

    def get_element(self):
        element = Waits.get_wait_one_visibility(self.by_locator)
        return element

    def get_elements(self):
        elements = Waits.get_wait_all_visibility(self.by_locator)
        return elements

    def get_text(self):
        return self.get_element().text
