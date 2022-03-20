from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def click_on_element(self, by_locator):
        self.driver.find_element(by_locator).click()

    def get_elements(self, by_locator):
        self.driver.find_elements(by_locator)

    def get_element(self, by_locator):
        return self.driver.find_element(by_locator)
