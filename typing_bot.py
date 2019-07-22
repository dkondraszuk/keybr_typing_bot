import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from urls import LOGGED_IN_URL, FIREFOX_EXE_PATH
from pages.account_page import AccountPage
from pages.practice_page import PracticePage
from keypress_emulator import Keyboard

options = Options()
# options.headless = True

driver = webdriver.Firefox(executable_path=FIREFOX_EXE_PATH)

driver.set_window_size(1440, 900)
driver.get(LOGGED_IN_URL)
print('Logged In')

# go to practice page
account = AccountPage(driver)
account.click_practice()
print('Went to Practice')

practice = PracticePage(driver)

# close popup window
practice.close_popup_window()

# get TextInput items
input_items = practice.find_text_input_items()
input_items_text = [' ' if item.text == '␣' else item.text for item in input_items]
input_text = ''.join(input_items_text)

# click to activate:
practice.click_to_activate()

# start typing:
keyboard = Keyboard()
keyboard.type_sentence(input_text)

time.sleep(5)  # fixme: only for testing
driver.quit()


# todo: Implement separate functions for the above functionality.
# todo: Implement function to change settings (extended lessons and alphabet)
