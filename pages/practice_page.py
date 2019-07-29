from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PracticePage:

    def __init__(self, driver):
        self._driver = driver
        self._text_input_item_class = 'TextInput-item'
        self._close_popup_class = 'Tour-close'
        self._click_to_practice_class = 'Practice-textInput'

    def find_text_input_items(self):
        elements = self._driver.find_elements_by_class_name(self._text_input_item_class)
        return elements

    def close_popup_window(self):
        try:
            wait = WebDriverWait(self._driver, 15)
            wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self._close_popup_class)))
        except TimeoutException:
            print('No pop-up window found.')
            return
        else:
            self._driver.find_element_by_class_name(self._close_popup_class).click()
            print('Closed pop-up window!')

    def click_to_activate(self):
        self._driver.find_element_by_class_name(self._click_to_practice_class).click()
        print('Practice field activated!')
