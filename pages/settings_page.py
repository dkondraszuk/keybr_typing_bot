from selenium.webdriver.common.action_chains import ActionChains

from constants import settings_constants as sc


class SettingsPage:

    def __init__(self, driver):
        self._driver = driver

    def extend_alphabet(self):
        slider = self._driver.find_element_by_xpath(sc.ALPHABET_SLIDER)
        # slider = self._driver.find_element_by_css_selector(sc.ALPHABET_SLIDER)
        move = ActionChains(self._driver)
        move.click_and_hold(slider).move_by_offset(288, 0).release().perform()
        print('Alphabet extended!')
