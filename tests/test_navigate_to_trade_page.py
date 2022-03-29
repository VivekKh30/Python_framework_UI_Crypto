from PageObject.TradePage import TradePage
from PageObject.HomePage import HomePage
from tests.test_basetest import BaseTest


class TestHomePage(BaseTest):

    def test_navigate_to_trade_page(self):
        homePage = HomePage(self.driver)
        tradePage = TradePage(self.driver)
        homePage.acceptPrerequisite()
        homePage.cryptoSelection('ZIL', '/USDT')
        assert tradePage.actual_crypto() == 'ZIL/USDT'
        assert self.driver.current_url == 'https://crypto.com/exchange/trade/spot/ZIL_USDT'
        tradePage.attributes_displayed()
