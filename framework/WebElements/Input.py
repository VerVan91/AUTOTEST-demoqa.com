from framework.Utils.Waits import Waits
from framework.WebElements.BaseElement import BaseElement


class Input(BaseElement):

    def send_keys(self, text, do_clear=True):
        element = Waits.get_wait_one_visibility(self.by_locator)
        if do_clear:
            element.clear()
            element.send_keys(text)
        else:
            element.send_keys(text)
