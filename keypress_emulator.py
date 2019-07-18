# Standard library imports...
import time

# Third-party imports...
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EXE_PATH = r'/home/dkondraszuk/dev/keybr_typing_bot/drivers/chromedriver'  # todo: use os.path or smth
URL = 'https://keybr.com'

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.set_window_size(1440, 900)
driver.implicitly_wait(10)
driver.get(URL)

driver.find_element_by_class_name('Tour-close').click()
print('Clicked!')

print(driver.page_source)

driver.quit()
