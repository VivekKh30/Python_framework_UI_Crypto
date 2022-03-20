import time

from PageObject.CartJourney import CartJourney
from PageObject.HomePage import HomePage
from PageObject.Login import Login
from PageObject.OrderHistory import OrderHistory
from tests.test_basetest import BaseTest


class TestHomePage(BaseTest):

    def test_item_purchase_women_category(self):
        login = Login(self.driver)
        homePage = HomePage(self.driver)
        cartJourney = CartJourney(self.driver)
        odderHistory = OrderHistory(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "Happy2022")
        homePage.selectMenu("Women")
        PRODUCT_PRICE = homePage.get_Product_Price()
        homePage.addToCart()
        time.sleep(5)
        PRODUCT_PRICE_ON_CART = homePage.get_Product_Price_In_Cart()
        assert PRODUCT_PRICE == PRODUCT_PRICE_ON_CART
        assert "Product successfully added to your shopping cart" in homePage.get_add_to_cart_success_msg()
        homePage.checkout()
        cartJourney.complete_Order_Journey()
        assert cartJourney.order_success_msg() == 'Your order on My Store is complete.'
        ref_id = cartJourney.get_Ref_Id()
        odderHistory.validate_Order_History()
        assert ref_id == odderHistory.get_order_history()

    def test_item_purchase_dresses_category(self):
        login = Login(self.driver)
        homePage = HomePage(self.driver)
        cartJourney = CartJourney(self.driver)
        odderHistory = OrderHistory(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "Happy2022")
        homePage.selectMenu("Dresses")
        PRODUCT_PRICE = homePage.get_Product_Price()
        homePage.addToCart()
        time.sleep(5)
        PRODUCT_PRICE_ON_CART = homePage.get_Product_Price_In_Cart()
        assert PRODUCT_PRICE == PRODUCT_PRICE_ON_CART
        assert "Product successfully added to your shopping cart" in homePage.get_add_to_cart_success_msg()
        homePage.checkout()
        cartJourney.complete_Order_Journey()
        assert cartJourney.order_success_msg() == 'Your order on My Store is complete.'
        ref_id = cartJourney.get_Ref_Id()
        odderHistory.validate_Order_History()
        assert ref_id == odderHistory.get_order_history()

    def test_item_purchase_tshirts_category(self):
        login = Login(self.driver)
        homePage = HomePage(self.driver)
        cartJourney = CartJourney(self.driver)
        odderHistory = OrderHistory(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "Happy2022")
        homePage.selectMenu("T-shirts")
        PRODUCT_PRICE = homePage.get_Product_Price()
        homePage.addToCart()
        time.sleep(5)
        PRODUCT_PRICE_ON_CART = homePage.get_Product_Price_In_Cart()
        assert PRODUCT_PRICE == PRODUCT_PRICE_ON_CART
        assert "Product successfully added to your shopping cart" in homePage.get_add_to_cart_success_msg()
        homePage.checkout()
        cartJourney.complete_Order_Journey()
        assert cartJourney.order_success_msg() == 'Your order on My Store is complete.'
        ref_id = cartJourney.get_Ref_Id()
        odderHistory.validate_Order_History()
        assert ref_id == odderHistory.get_order_history()

    def test_item_purchase_multiple_category(self):
        login = Login(self.driver)
        homePage = HomePage(self.driver)
        cartJourney = CartJourney(self.driver)
        odderHistory = OrderHistory(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "Happy2022")
        homePage.selectMenu("Women")
        PRODUCT_PRICE_WOMEN = homePage.get_Product_Price()
        homePage.addToCart()
        homePage.continueShopping()
        homePage.selectMenu("Dresses")
        PRODUCT_PRICE_DRESSES = homePage.get_Product_Price()
        PRODUCT_PRICE = float(PRODUCT_PRICE_WOMEN.strip('$')) + float(PRODUCT_PRICE_DRESSES.strip('$'))
        homePage.addToCart()
        time.sleep(5)
        PRODUCT_PRICE_ON_CART = homePage.get_Product_Price_In_Cart()
        assert round(PRODUCT_PRICE, 2) == float(PRODUCT_PRICE_ON_CART.strip('$'))
        assert "Product successfully added to your shopping cart" in homePage.get_add_to_cart_success_msg()
        homePage.checkout()
        cartJourney.complete_Order_Journey()
        assert cartJourney.order_success_msg() == 'Your order on My Store is complete.'
        ref_id = cartJourney.get_Ref_Id()
        odderHistory.validate_Order_History()
        assert ref_id == odderHistory.get_order_history()
