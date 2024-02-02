from Constants.HomePageConstants import HOMEPAGE_CONSTANTS
from Pages.BasePage import BasePage
from Locators.HomePageLocators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self):
        """Waits till Edge client page is loaded
        :returns: nothing
        """
        self.wait_for_page_url(HOMEPAGE_CONSTANTS.HOME_PAGE_URL)
        self.wait_for_element_visibility(HomePageLocators.HOMEPAGE_ELEMENT)

    def click_market_data(self, navbar_menu):
        """To click market data sub-menu in Solutions navbar menu
        :param navbar_menu: Main menu label, where the sub-menu needs to clicked in present"""
        elements = self.get_all_elements(HomePageLocators.NAVBAR_OPTIONS)
        sub_element = self.get_element(HomePageLocators.SOLUTIONS_SUB_MENU)
        for element in elements:
            if element.text == navbar_menu:
                self.hover_on_element_and_click(element, sub_element)
                break

    def handle_cookies(self, target_locator):
        """To accept or decline the cookies alert in the homepage
        :param target_locator : the target locator object"""
        self.wait_for_element_visibility(target_locator)
        self.click(target_locator)

