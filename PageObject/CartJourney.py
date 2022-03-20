from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass


class CartJourney(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    CHECKOUT_OPTION = (By.XPATH, "(//*[@title='Proceed to checkout'])[2]")
    SUBMIT_BUTTON = (By.XPATH, "(//button[@type='submit'])[2]")
    TERMS_CONDITIONS = (By.ID, "uniform-cgv")
    PAY_BY_BANK_WIRE = (By.XPATH, "//*[@class='bankwire']")
    CONFIRM_ORDER_OPTION = (By.XPATH, "(//button[@type='submit'])[2]")
    SUCCESS_MSG = (By.XPATH, "//*[text()='Your order on My Store is complete.']")
    ORDER_REF_HISTORY = (By.XPATH, "(//td[@class='history_link bold footable-first-column'])[1]")
    ORDER_REF = (By.XPATH, "//div[@class='box']")
    REF_ID = ''

    def addressConfirmation(self):
        self.click_element(self.CHECKOUT_OPTION)

    def shipping(self):
        self.click_element(self.SUBMIT_BUTTON)
        self.click_element(self.TERMS_CONDITIONS)
        self.click_element(self.SUBMIT_BUTTON)

    def payment(self):
        self.click_element(self.PAY_BY_BANK_WIRE)

    def confirmOrder(self):
        self.click_element(self.CONFIRM_ORDER_OPTION)
        self.get_Ref_Id()

    def get_Ref_Id(self):
        messages = self.get_element_text(self.ORDER_REF).splitlines()
        for message in messages:
            if "Do not forget to insert your order reference" in message:
                self.REF_ID = message[47:56]
                break
        return self.REF_ID

    def complete_Order_Journey(self):
        self.addressConfirmation()
        self.shipping()
        self.payment()
        self.confirmOrder()

    def order_success_msg(self):
        return self.get_element_text(self.SUCCESS_MSG)
