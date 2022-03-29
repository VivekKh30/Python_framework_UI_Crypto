from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass


class TradePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    ACTUAL_CRYPTO_DETAILS = (By.XPATH, "//*[@class='toggle']")
    BUY_BUTTON = (By.XPATH, "//div[text()=' Buy ']")
    SELL_BUTTON = (By.XPATH, "//div[text()=' Sell ']")
    HIGH = (By.XPATH, "//div[@class='desktop-symbol']/div[3]")
    LOW = (By.XPATH, "//div[@class='desktop-symbol']/div[4]")
    CHANGE = (By.XPATH, "//div[@class='desktop-symbol']/div[2]")
    LOGIN_BUTTON = (By.XPATH, "(//*[text()=' Login or Sign Up '])[1]")
    VOLUME = (By.XPATH, "//div[@class='desktop-symbol']/div[5]")

    def actual_crypto(self):
        return self.get_element_text(self.ACTUAL_CRYPTO_DETAILS)

    def attributes_displayed(self):
        self.is_element_displayed(self.BUY_BUTTON)
        self.is_element_displayed(self.SELL_BUTTON)
        self.is_element_displayed(self.HIGH)
        self.is_element_displayed(self.LOW)
        self.is_element_displayed(self.CHANGE)
        self.is_element_displayed(self.LOGIN_BUTTON)
        self.is_element_displayed(self.VOLUME)
