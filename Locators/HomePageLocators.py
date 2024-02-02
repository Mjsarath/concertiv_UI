from selenium.webdriver.common.by import By


class HomePageLocators():
    HOMEPAGE_ELEMENT = (By.CLASS_NAME,'navbar_container')
    NAVBAR_OPTIONS = (By.CLASS_NAME,'navbar-link')
    SOLUTIONS_SUB_MENU = (By.XPATH,"//div[@class='navbar_item']/div[text()='Market Data']")
    ACCEPT_COOKIE = (By.ID,'hs-eu-confirmation-button')
    DECLINE_COOKIE = (By.ID,'hs-eu-decline-button')