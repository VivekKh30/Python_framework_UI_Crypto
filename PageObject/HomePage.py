import time
from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    ACCEPT_COOKIES = (By.XPATH, "//button[@title='Accept Cookies']")
    DISCLAIMER = (By.XPATH, "//button[text()='Next']")
    ACCEPT_DISCLAIMER = (By.XPATH, "//button[text()='Accept']")
    CRYPTO_SELECTION_XPATH = "//span[text()={name}]/following-sibling::span[text()={currency}]"

    def acceptPrerequisite(self):
        self.click_element(self.DISCLAIMER)
        time.sleep(2)
        self.click_element(self.ACCEPT_COOKIES)
        time.sleep(2)
        self.click_element(self.ACCEPT_DISCLAIMER)

    def cryptoSelection(self, name, currency):
        CRYPTO_SELECTION_XPATH = self.CRYPTO_SELECTION_XPATH.format(name="'" + name + "'",
                                                                    currency="'" + currency + "'")
        tradeButton = self.driver.find_element(By.XPATH, CRYPTO_SELECTION_XPATH)
        self.driver.execute_script("arguments[0].click();", tradeButton)
