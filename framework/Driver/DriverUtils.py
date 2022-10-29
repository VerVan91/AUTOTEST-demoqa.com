from framework.Driver.WebDriver import WebDriver


class DriverUtils:

    @staticmethod
    def switch_to_frame(frame_name):
        WebDriver.get_driver().switch_to.frame(frame_name)

    @staticmethod
    def switch_to_default_frame():
        WebDriver.get_driver().switch_to.default_content()

    @staticmethod
    def switch_to_last_tab():
        WebDriver.get_driver().switch_to.window(WebDriver.get_driver().window_handles[-1])

    @staticmethod
    def switch_to_first_tab():
        WebDriver.get_driver().switch_to.window(WebDriver.get_driver().window_handles[0])

    @staticmethod
    def close_current_tab():
        WebDriver.get_driver().close()
