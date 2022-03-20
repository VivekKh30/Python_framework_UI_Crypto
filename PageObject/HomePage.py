import time
from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    WOMEN_MENU = (By.XPATH, "//a[@title='Women']")
    MENU_SELECTION = (By.XPATH, "//*[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li")
    ITEM_SELECTION = (By.XPATH, "(//div[@class='right-block'])[1]")
    CONTINUE_SHOPPING = (By.XPATH, '//*[@title="Continue shopping"]')
    ADD_TO_CART = (By.XPATH, "(//*[@title='Add to cart'])[1]")
    CHECKOUT_BTN = (By.XPATH, "//*[@title='Proceed to checkout']")
    PRODUCT_PRICE = (By.XPATH, "(//span[@class='price product-price'])[2]")
    PRODUCT_PRICE_ON_CART = (By.XPATH, "//*[@class='ajax_block_products_total']")
    SUCCESS_ADD_TO_CART_MSG = (By.XPATH, "//div[@class='layer_cart_product col-xs-12 col-md-6']/h2")
    section = []

    def selectMenu(self, menuOption):
        time.sleep(2)
        sections = self.driver.find_elements(*HomePage.MENU_SELECTION)
        for section in sections:
            if section.text.lower() == menuOption.lower():
                section.click()
                break

    def continueShopping(self):
        self.click_element(self.CONTINUE_SHOPPING)

    def addToCart(self):
        button = self.driver.find_element(*HomePage.ITEM_SELECTION)
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        self.click_element(self.ADD_TO_CART)

    def checkout(self):
        self.click_element(self.CHECKOUT_BTN)

    def get_Product_Price(self):
        return self.get_element_text(self.PRODUCT_PRICE)

    def get_Product_Price_In_Cart(self):
        return self.get_element_text(self.PRODUCT_PRICE_ON_CART)

    def get_add_to_cart_success_msg(self):
        return self.get_element_text(self.SUCCESS_ADD_TO_CART_MSG)
