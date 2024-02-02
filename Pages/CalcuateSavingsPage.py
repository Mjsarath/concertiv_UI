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

    def enter_professional_firm_input(self, count):
        """To enter/slide the given count in the professional firm input field
        :param count: offset value that needs to be updated"""
        self.slide_into_given_value(CalculateSavingsLocators.PROFESSIONAL_FIRM_COUNT, count)

    def select_firm(self, firm_name):
        """To select the desired Vendor labels in Calculate savings page
        :param firm_name: Vendor name that needs to be selected"""
        elements = self.get_all_elements(CalculateSavingsLocators.MARKET_DATA_VENDOR)
        for ele in elements:
            if ele.text == firm_name:
                self.click(ele)
                break

    def verify_vendor_selected(self, vendor_name):
        """To verify the selected vendor in calculate savings page
        :param vendor_name : Expected vendor name
        :returns : returns True when the vendor selected is correct, else returns False"""
        element = self.driver.find_element(By.XPATH,
                                           CalculateSavingsPageConstants.VENDOR_CHECKBOX.format(value=vendor_name))
        if element.get_attribute("checked"):
            return True
        return False

    def get_estimate(self, estimate_name):
        """To get the estimation values that is updated based on the firm and vendor selection
        :param estimate_name: Estimation title that needs to be returned
        :returns : estimate value of given label"""
        element = self.driver.find_element(By.XPATH,
                                           CalculateSavingsPageConstants.ESTIMATE_VALUE.format(value=estimate_name))
        return element.text

    def verify_input_firm_value(self, target_locator, value):
        """To verify the entered/slided input
        :param target_locator: the target locator object
        :param value: Expected value that needs to be verified
        :returns : True when the value is correct, else returns false"""
        element = self.get_element(target_locator)
        if element.text == value:
            return True
        return False
