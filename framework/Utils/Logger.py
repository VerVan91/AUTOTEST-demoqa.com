import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger("Test Login")
        file_handler = logging.FileHandler('logs.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

    @staticmethod
    def log_info(text):
        Logger().logger.info(text)

    @staticmethod
    def log_warning(text):
        Logger().logger.warning(text)

    @staticmethod
    def log_error(text):
        Logger().logger.error(text)
