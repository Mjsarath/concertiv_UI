from Pages.BasePage import BasePage
from Pages.HomePage import HomePage

class MarketDataPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.homepage = HomePage(self.driver)
