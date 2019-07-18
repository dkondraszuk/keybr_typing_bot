import os
import urllib.parse

# page urls:
BASE_URL = 'https://www.keybr.com/login/'
AUTH_KEY = os.environ.get('KEYBR_KEY')

LOGGED_IN_URL = urllib.parse.urljoin(BASE_URL, AUTH_KEY)

# driver exe path:
CHROME_DRIVER = 'drivers/chromedriver'
CHROME_EXE_PATH = os.path.abspath(CHROME_DRIVER)
