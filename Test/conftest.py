from selenium import webdriver
import pytest
import warnings



@pytest.fixture()
def setup(request):
    global browser
    browser = "chrome"
    app_url = 'https://www.concertiv.com/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    web_driver = webdriver.Chrome(
        options=options)
    warnings.filterwarnings("ignore")

    request.cls.driver = web_driver
    web_driver.get(app_url)
    web_driver.maximize_window()
    return web_driver
