from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass


class OrderHistory(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    MY_PROFILE = (By.XPATH, "//*[@class='account']")
    ORDER_HISTORY = (By.XPATH, "//*[@title='Orders']")
    ORDER_REF = (By.XPATH, "(//*[@class='color-myaccount'])[1]")

    def selectProfile(self):
        self.click_element(self.MY_PROFILE)

    def selectOrderHistory(self):
        self.click_element(self.ORDER_HISTORY)

    def validate_Order_History(self):
        self.selectProfile()
        self.selectOrderHistory()

    def get_order_history(self):
        return self.get_element_text(self.ORDER_REF)
