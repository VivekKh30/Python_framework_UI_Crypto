import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


driver = None
URL = "https://crypto.com/exchange/markets"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    global driver
    if browser_name == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("detach", True)
        d = DesiredCapabilities.CHROME
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
        driver.get(URL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver
    yield
    driver.close()
