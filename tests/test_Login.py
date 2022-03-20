from PageObject.Login import Login
from tests.test_basetest import BaseTest


class TestHomePage(BaseTest):

    def test_Successful_LogIn(self):
        login = Login(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "Happy2022")
        assert self.driver.find_element(*Login.LOGOUT).is_displayed()
        assert self.driver.current_url == login.SUCCESS_LOGIN_URL

    def test_Password_Missing_Error(self):
        login = Login(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "")
        assert self.driver.find_element(*Login.PSWD_FAILURE_MSG).is_displayed()

    def test_Invalid_Password_Error(self):
        login = Login(self.driver)
        login.perform_login("tonapedipti@yahoo.in", "Test123")
        assert self.driver.find_element(*Login.PSWD_INVALID_MSG).is_displayed()

    def test_Invalid_Username_Error(self):
        login = Login(self.driver)
        login.perform_login("", "Test123")
        assert self.driver.find_element(*Login.USERNAME_INVALID_MSG).is_displayed()
