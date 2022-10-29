import json


class DataUtils:
    TEST_DATA_FILE = '../Data/TestData.json'
    CONFIG_DATA_FILE = '../Data/ConfigData.json'

    @staticmethod
    def data_json(url):
        with open(url) as f:
            content = f.read()
            content_dict = json.loads(content)
        return content_dict

    @classmethod
    def test_data_json(cls):
        return cls.data_json(cls.TEST_DATA_FILE)

    @classmethod
    def config_data_json(cls):
        return cls.data_json(cls.CONFIG_DATA_FILE)

    @classmethod
    def handling_data_for_table(cls):
        user_data_dict = cls.test_data_json()["tables_test_data"][0]
        del user_data_dict["User number"]
        return user_data_dict.values()
