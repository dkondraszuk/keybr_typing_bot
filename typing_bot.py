# Standard library imports...
import time

# Third-party imports...
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Local imports...
from urls import LOGGED_IN_URL, CHROME_EXE_PATH

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=CHROME_EXE_PATH)
driver.set_window_size(1440, 900)
driver.implicitly_wait(10)
driver.get(LOGGED_IN_URL)

print(driver.page_source)

driver.quit()
