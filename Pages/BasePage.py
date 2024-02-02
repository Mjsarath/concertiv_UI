import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.web_driver_timeout = 10

    def click(self, element):
        """To click the desired web element (Waits till the element is visible)
        :param : element - Web element that needs to be clicked"""
        WebDriverWait(self.driver, self.web_driver_timeout).until(EC.element_to_be_clickable(element)).click()

    def get_page_title(self):
        """To return the title of the current page
        :returns: Title of the page"""
        return self.driver.title

    def get_page_url(self):
        """To return the updated url
        :returns: returns the URL of the page"""
        return self.driver.current_url

    def wait_for_page_url(self, page_url):
        """Waits for the page to be loaded
        :param:page_url - URL that needs to be waited for or loaded
        :returns: True-when the URL is loaded
        """
        WebDriverWait(self.driver, self.web_driver_timeout).until(EC.url_contains(page_url))
        return True

    def navigate_to_url(self, page_url):
        """To change the URL to the desired page
        :param: page_url - URL that needs to be changed"""
        self.driver.get(page_url)

    def get_text(self, element):
        """To get the element text
        :param element : The locator from which the text needs to be returned
        :returns Text of the element"""
        locator = WebDriverWait(self.driver, self.web_driver_timeout).until(EC.presence_of_element_located(element))
        return locator.text.strip()

    def get_all_elements(self, target_locator, no_wait=False):
        """To get all the element instance from the DOM
        :returns : The list of web element """
        return WebDriverWait(self.driver, self.web_driver_timeout).until(
            EC.presence_of_all_elements_located(target_locator))

    def scroll_to_element(self, target_locator):
        """To scroll the page to the target locator given
        :param : target_locator - to where the scope of the page should move
        """
        self.driver.execute_script("argument[0].scrollIntoView();", target_locator)

    def scroll_page_down(self):
        """To scroll the page down to the given range"""
        self.driver.execute_script("window.scrollBy(0,300);")

    def get_element(self, target_locator, no_wait=False):
        """Returns element matching the locator as Selenium Webelement

        :param target_locator: The target locator
        :param no_wait: Set to True to fetch the element directly without
        waiting. Defaults to False.
        :returns: the found element as a Selenium Webelement
        """
        if no_wait:
            EC.presence_of_element_located(target_locator)
        else:
            return WebDriverWait(self.driver, self.web_driver_timeout).until(
                EC.presence_of_element_located(target_locator))

    def is_element_invisible(self, target_locator):
        """Checks whether the target element is not present
        :param target_locator: The target locator
        :return: True is not present, raises exception if present
        """
        try:
            WebDriverWait(self.driver, self.web_driver_timeout / 2).until(
                EC.invisibility_of_element_located(target_locator))
            return True
        except Exception as _err:
            return False

    def wait_for_page_loader_to_finish(self):
        """Waits for the page loader to go away if present
        :return:  True is visible, else raises exception
        """
        try:
            self.get_element("BasePageLocators.PAGE_LOADER")
            self.is_element_invisible("BasePageLocators.PAGE_LOADER")
            time.sleep(1)
        except Exception as err:
            pass
        return True

    def wait_for_element_visibility(self, target_locator):
        """Waits for element to be visible

        :param target_locator: The target locator object
        :returns : returns True if element is visible, raises exception if
        fails
        """
        WebDriverWait(self.driver, self.web_driver_timeout).until(
            EC.presence_of_element_located(target_locator))
        return True

    def switch_to_frame(self, frame=0):
        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def hover_on_element_and_click(self, target_locator, sub_menu):
        ac = ActionChains(self.driver)
        ac.move_to_element(target_locator).click(sub_menu).perform()

    def slide_into_given_value(self,target_locator, input_value):
        ac = ActionChains(self.driver)
        element = self.get_element(target_locator)
        ac.click_and_hold(element).move_by_offset(input_value,0).release().perform()

    def verify_page_loaded_successfully(self,target_locator):

        return self.wait_for_element_visibility(target_locator)