from selenium.webdriver.common.by import By
from Utility.BaseClass import BaseClass


class Login(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    SIGNIN = (By.XPATH, "//a[@class='login']")
    ID = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    SUBMIT = (By.ID, "SubmitLogin")
    LOGOUT = (By.XPATH, "//*[@class='logout']")
    PSWD_FAILURE_MSG = (By.XPATH, "//li[text()='Password is required.']")
    PSWD_INVALID_MSG = (By.XPATH, "//li[text()='Authentication failed.']")
    USERNAME_INVALID_MSG = (By.XPATH, "//li[text()='An email address required.']")
    SUCCESS_LOGIN_URL = 'http://automationpractice.com/index.php?controller=my-account'

    def selectSignInOption(self):
        self.click_element(self.SIGNIN)

    def enterId(self, username):
        self.enter_text(self.ID, username)

    def enterPassword(self, password):
        self.enter_text(self.PASSWORD, password)

    def submitLogInDetails(self):
        self.click_element(self.SUBMIT)

    def perform_login(self, username, password):
        self.selectSignInOption()
        self.enterId(username)
        self.enterPassword(password)
        self.submitLogInDetails()
