import time

from Constants.CalculateSavingsPageConstants import CalculateSavingsPageConstants
from Constants.MarketDataPageConstants import MarketDataPageConstants
from Locators.CalculateSavingsPageLocators import CalculateSavingsLocators
from Locators.HomePageLocators import HomePageLocators
from Locators.MarketDataPageLocators import MarketDataPageLocators
from Pages.CalcuateSavingsPage import CalculateSavingsPage
from Pages.HomePage import HomePage
from Pages.MarketDataPage import MarketDataPage
from Test.test_base import BaseTest
from Constants.HomePageConstants import HOMEPAGE_CONSTANTS


class TestConcertiv(BaseTest):

    def test_launch_app(self):
        """To test the application is launched and the homepage is successfully loaded"""
        self.homepage = HomePage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        assert self.homepage.verify_page_loaded_successfully(HomePageLocators.HOMEPAGE_ELEMENT)
        self.homepage.driver.quit()

    def test_select_market_data_menu(self):
        """To test the Market Data page is navigated and loaded successfully"""
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        assert self.market_datapage.verify_page_loaded_successfully(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        self.homepage.driver.quit()

    def test_navigate_calculate_saving(self):
        """To test the calculate savings page navigated and successfully loaded """
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        assert self.calculate_page.verify_page_loaded_successfully(CalculateSavingsLocators.CALCULATOR_CLASS)
        self.homepage.driver.quit()

    def test_set_value_for_professional_firm(self):
        """To test the value is set to the professional firm input field and verify the value selected"""
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        self.calculate_page.switch_to_frame()
        self.calculate_page.enter_professional_firm_input(CalculateSavingsPageConstants.PROFESSIONAL_FIRM_INPUT)
        self.calculate_page.scroll_page_down()
        status = self.calculate_page.verify_input_firm_value(CalculateSavingsLocators.UPDATED_FIRM_COUNT,
                                                             CalculateSavingsPageConstants.SLIDER_VALUE)
        assert status
        self.homepage.driver.quit()

    def test_select_and_verify_firm_menu(self):
        """To Test the desired vendor is selected from the given menu"""
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        self.calculate_page.switch_to_frame()
        self.calculate_page.enter_professional_firm_input(CalculateSavingsPageConstants.PROFESSIONAL_FIRM_INPUT)
        self.calculate_page.scroll_page_down()
        self.calculate_page.select_firm(CalculateSavingsPageConstants.VENDOR_NAME)
        assert self.calculate_page.verify_vendor_selected(CalculateSavingsPageConstants.VENDOR_NAME)
        self.homepage.driver.quit()

    def test_check_estimate_and_savings(self):
        """To test the estimate and savings of the base savings and top spend"""
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        self.calculate_page.switch_to_frame()
        self.calculate_page.enter_professional_firm_input(CalculateSavingsPageConstants.PROFESSIONAL_FIRM_INPUT)
        self.calculate_page.select_firm(CalculateSavingsPageConstants.VENDOR_NAME)
        self.calculate_page.scroll_page_down()
        time.sleep(2)
        base_spend = self.calculate_page.get_estimate(CalculateSavingsPageConstants.BASE_CASE_SAVINGS_LABEL)
        top_spend = self.calculate_page.get_estimate(CalculateSavingsPageConstants.TOP_SPEND_LABEL)
        self.calculate_page.switch_to_default()
        assert top_spend < base_spend
        self.homepage.driver.quit()