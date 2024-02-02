import time

from selenium.webdriver.common.by import By

from Constants.CalculateSavingsPageConstants import CalculateSavingsPageConstants
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Locators.CalculateSavingsPageLocators import CalculateSavingsLocators


class CalculateSavingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.homepage = HomePage(self.driver)

    def professional_firm_input(self, count):
        self.slide_into_given_value(CalculateSavingsLocators.PROFESSIONAL_FIRM_COUNT, count)

    def select_firm(self, firm_name):
        elements = self.get_all_elements(CalculateSavingsLocators.MARKET_DATA_VENDOR)
        for ele in elements:
            if ele.text == firm_name:
                self.click(ele)
                break

    def verify_vendor_selected(self, vendor_name):
        element = self.driver.find_element(By.XPATH,
                                             CalculateSavingsPageConstants.VENDOR_CHECKBOX.format(value=vendor_name))
        if element.get_attribute("checked"):
            return True
        return False

    def get_estimate(self, estimate_name):
        element = self.driver.find_element(By.XPATH,
                                           CalculateSavingsPageConstants.ESTIMATE_VALUE.format(value=estimate_name))
        return element.text

    def verify_input_firm_value(self, target_locator, value, index=0):
        element = self.get_element(target_locator)

        if element.text == value:
            return True
        return False
