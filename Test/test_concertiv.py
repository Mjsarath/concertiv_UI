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
        self.homepage = HomePage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        assert self.homepage.verify_page_loaded_successfully(HomePageLocators.HOMEPAGE_ELEMENT)
        self.homepage.driver.quit()

    def test_select_market_data_menu(self):
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU,
                                        HOMEPAGE_CONSTANTS.MARKET_DATA_SUB_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        assert self.market_datapage.verify_page_loaded_successfully(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        self.homepage.driver.quit()

    def test_navigate_calculate_saving(self):
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU,
                                        HOMEPAGE_CONSTANTS.MARKET_DATA_SUB_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        assert self.calculate_page.verify_page_loaded_successfully(CalculateSavingsLocators.CALCULATOR_CLASS)
        self.homepage.driver.quit()

    def test_set_value_for_professional_firm(self):
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU,
                                        HOMEPAGE_CONSTANTS.MARKET_DATA_SUB_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        self.calculate_page.switch_to_frame()
        self.calculate_page.professional_firm_input(50)
        self.calculate_page.scroll_page_down()
        status = self.calculate_page.verify_input_firm_value(CalculateSavingsLocators.UPDATED_FIRM_COUNT,
                                                             CalculateSavingsPageConstants.SLIDER_VALUE)
        assert status
        self.homepage.driver.quit()

    def test_select_and_verify_firm_menu(self):
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU,
                                        HOMEPAGE_CONSTANTS.MARKET_DATA_SUB_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        self.calculate_page.switch_to_frame()
        self.calculate_page.professional_firm_input(50)
        self.calculate_page.scroll_page_down()
        self.calculate_page.select_firm(CalculateSavingsPageConstants.VENDOR_NAME)
        assert self.calculate_page.verify_vendor_selected(CalculateSavingsPageConstants.VENDOR_NAME)
        self.homepage.driver.quit()

    def test_check_estimate_and_savings(self):
        self.homepage = HomePage(self.driver)
        self.market_datapage = MarketDataPage(self.driver)
        self.calculate_page = CalculateSavingsPage(self.driver)
        self.homepage.wait_for_page_load()
        self.homepage.handle_cookies(HomePageLocators.DECLINE_COOKIE)
        self.homepage.click_market_data(HOMEPAGE_CONSTANTS.SOLUTION_NAVBAR_MENU,
                                        HOMEPAGE_CONSTANTS.MARKET_DATA_SUB_MENU)
        self.market_datapage.wait_for_page_url(MarketDataPageConstants.PageURL)
        self.market_datapage.click(MarketDataPageLocators.CALCULATE_SAVING_BUTTON)
        time.sleep(5)
        self.calculate_page.scroll_page_down()
        self.calculate_page.switch_to_frame()
        self.calculate_page.professional_firm_input(50)
        self.calculate_page.scroll_page_down()
        self.calculate_page.select_firm(CalculateSavingsPageConstants.VENDOR_NAME)
        base_spend = self.calculate_page.get_estimate(CalculateSavingsPageConstants.BASE_CASE_SAVINGS_LABEL)
        top_spend = self.calculate_page.get_estimate(CalculateSavingsPageConstants.TOP_SPEND_LABEL)
        self.calculate_page.switch_to_default()
        assert top_spend < base_spend
        self.homepage.driver.quit()

