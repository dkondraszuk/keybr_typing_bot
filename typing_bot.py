# Standard library imports...
import time

# Third-party imports...
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Local imports...
from urls import LOGGED_IN_URL, CHROME_EXE_PATH, FIREFOX_EXE_PATH
from pages.account_page import AccountPage
from pages.practice_page import PracticePage

# options = Options()
# options.headless = True

# Chrome
# driver = webdriver.Chrome(executable_path=CHROME_EXE_PATH)

# Firefox
driver = webdriver.Firefox(executable_path=FIREFOX_EXE_PATH)
driver.set_window_size(1440, 900)
# driver.implicitly_wait(10)
# driver.set_page_load_timeout(15)
# driver.get(LOGGED_IN_URL)

driver.get(LOGGED_IN_URL)

print('Logged In')
# driver.find_elements_by_class_name('TextInput-item').text
# go to practice page
account = AccountPage(driver)
account.click_practice()
print('Went to Practice')


practice = PracticePage(driver)

# close popup window
practice.close_popup_window()

# get TextInput items
text_input_items = practice.find_text_input_items()
for item in text_input_items:
    print(item.text)

time.sleep(120)

driver.quit()
