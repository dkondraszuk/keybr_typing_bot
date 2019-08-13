import random
import time

from pynput.keyboard import Controller


class Keyboard:

    def __init__(self):
        self._keyboard = Controller()

    @staticmethod
    def _generate_typing_delay():
        delay = random.uniform(0.06, 0.10)
        return round(delay, 3)

    def type_sentence(self, sentence):
        for char in sentence:
            self._keyboard.press(char)
            self._keyboard.release(char)
            delay = self._generate_typing_delay()
            time.sleep(delay)
