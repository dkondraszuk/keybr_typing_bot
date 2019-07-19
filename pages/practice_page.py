from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PracticePage:

    def __init__(self, driver):
        self.driver = driver
        self.text_input_item_class = 'TextInput-item'
        self.close_popup_class = 'Tour-close'

    def find_text_input_items(self):
        elements = self.driver.find_elements_by_class_name(self.text_input_item_class)
        return elements

    def close_popup_window(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.close_popup_class)))
        except TimeoutException:
            print('No pop-up window found.')
            return
        else:
            self.driver.find_element_by_class_name(self.close_popup_class).click()
            print('Closed pop-up window!')
