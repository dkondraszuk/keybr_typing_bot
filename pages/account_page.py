class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        # self.practice_button_link_text = 'Practice typing lessons'
        self.practice_button_link_text = 'Practice'

    def click_practice(self):
        self.driver.find_element_by_link_text(self.practice_button_link_text).click()
        # self.driver.find_elements_by_partial_link_text(self.practice_button_link_text).click()

