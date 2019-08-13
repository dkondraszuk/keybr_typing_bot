from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import practice_constants as pc


class PracticePage:

    def __init__(self, driver):
        self._driver = driver

    def find_text_input_items(self):
        elements = self._driver.find_elements_by_class_name(pc.TEXT_INPUT_ITEM)
        return elements

    def close_popup_window(self):
        try:
            wait = WebDriverWait(self._driver, 15)
            wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, pc.CLOSE_POPUP)))
        except TimeoutException:
            print('No pop-up window found.')
            return
        else:
            self._driver.find_element_by_class_name(pc.CLOSE_POPUP).click()
            print('Closed pop-up window!')

    def click_to_activate(self):
        self._driver.find_element_by_xpath(pc.CLICK_TO_PRACTICE).click()
        print('Practice field activated!')

    def go_to_settings(self):
        self._driver.find_element_by_xpath(pc.SETTINGS_BUTTON).click()
        print('Went to Settings!')
