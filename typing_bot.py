import time

from selenium.webdriver import Firefox

import urls
from constants import timers
from keypress_emulator import Keyboard
from pages.account_page import AccountPage
from pages.practice_page import PracticePage
from pages.settings_page import SettingsPage


class TypingBot:
    def __init__(self):
        self._driver = Firefox(executable_path=urls.FIREFOX_EXE_PATH)
        self._setup_driver()
        self._account = AccountPage(self._driver)
        self._practice = PracticePage(self._driver)
        self._settings = SettingsPage(self._driver)
        self._keyboard = Keyboard()

    def _setup_driver(self):
        self._driver.set_window_size(1440, 900)
        self._driver.implicitly_wait(timers.IMPLICIT_WAIT)

    def login(self):
        self._driver.get(urls.LOGGED_IN_URL)
        print('Logged In!')

    def go_to_practice(self):
        self._account.click_practice()
        self._practice.close_popup_window()

    def change_settings(self):
        self._practice.go_to_settings()
        self._settings.extend_alphabet()
        self._settings.extend_lesson_length()
        self._settings.enable_capital_letters()
        self._settings.enable_punctuation_characters()
        self._settings.save_settings()

    def practice_for_repetitions(self, practice_reps=1):
        for i in range(practice_reps):
            input_text = self._get_text_input_items()
            self._keyboard.type_sentence(input_text)
            time.sleep(timers.WAIT_FOR_NEXT_PRACTICE)

    def cleanup(self):
        self._driver.quit()

    def _get_text_input_items(self):
        input_items = self._practice.find_text_input_items()
        input_items_text = [' ' if item.text == '␣' else item.text for item in input_items]
        input_text = ''.join(input_items_text)
        return input_text
