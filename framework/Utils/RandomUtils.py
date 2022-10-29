from random import randint


class RandomUtils:
    @staticmethod
    def generate_random_text():
        return str(randint(0, 10))
