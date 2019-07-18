class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.practice_button_link_text = 'Practice typing lessons'

    def go_practice(self):
        self.driver.find_element_by_link_text(self.practice_button_link_text).click()

