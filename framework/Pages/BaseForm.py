from framework.Utils.Logger import Logger
from framework.Utils.Waits import Waits


class BaseForm:

    def __init__(self, by_locator, name):
        self.by_locator = by_locator
        self.name = name
        Logger.log_info(f"{self.name} is opened")

    def is_form_open(self):
        elements = Waits.get_wait_all_visibility(self.by_locator)
        if len(elements) == 0:
            return False
        return bool(elements)
