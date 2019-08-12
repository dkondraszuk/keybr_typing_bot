import time

from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions

import constants as cons
import urls
from keypress_emulator import Keyboard
from pages.account_page import AccountPage
from pages.practice_page import PracticePage


class TypingBot:
    def __init__(self, browser=cons.FIREFOX):
        self._browser = browser
        self._driver = None
        self._set_driver()
        self._account = AccountPage(self._driver)
        self._practice = PracticePage(self._driver)
        self._keyboard = Keyboard()

    def _set_driver(self):
        if self._browser == cons.FIREFOX:
            self._driver = Firefox(executable_path=urls.FIREFOX_EXE_PATH)
            options = FOptions()
        else:
            self._driver = Chrome(executable_path=urls.CHROME_EXE_PATH)
            options = COptions()
        options.headless = True
        self._driver.set_window_size(1440, 900)

    def login(self):
        self._driver.get(urls.LOGGED_IN_URL)
        print('Logged In!')

    def go_to_practice(self):
        self._account.click_practice()
        print('Went to Practice page!')

    def practice_for_specified_time(self, practice_time=5):
        self._practice.close_popup_window()
        self._practice.click_to_activate()
        practice_time_sec = 60 * practice_time
        t_start = time.time()
        while time.time() < t_start + practice_time_sec:
            input_text = self._get_text_input_items()
            self._keyboard.type_sentence(input_text)

    def cleanup(self):
        self._driver.quit()

    def _get_text_input_items(self):
        input_items = self._practice.find_text_input_items()
        input_items_text = [' ' if item.text == '␣' else item.text for item in input_items]
        input_text = ''.join(input_items_text)
        return input_text


if __name__ == '__main__':
    bot = TypingBot(browser=cons.FIREFOX)
    bot.login()
    bot.go_to_practice()
    bot.practice_for_specified_time(practice_time=5)
    bot.cleanup()

# todo: Implement separate functions for the above functionality.
# todo: Implement function to change settings (extended lessons and alphabet)
