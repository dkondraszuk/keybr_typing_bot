from constants import account_constants as ac


class AccountPage:

    def __init__(self, driver):
        self._driver = driver

    def click_practice(self):
        self._driver.find_element_by_xpath(ac.PRACTICE_BUTTON).click()
        print('Went to Practice!')
