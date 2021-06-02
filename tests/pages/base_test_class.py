import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import CreateLocators as CL
from utils import page_factory


class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.authentication_page = page_factory.authentication_page(self.driver)
        self.home_page = page_factory.home_page(self.driver)
        print('Class driver initialized')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('Class driver finished')

    def get_element_text_value(self, element_locator):
        """Gets text value of web element
                :param element_locator: webpage element xpath
                :return: None
        """
        self.visibility_of_element_wait(self.driver, element_locator)
        return self.driver.find_element_by_xpath(element_locator).text

    def click_button(self, button_xpath):
        """Click action on given button xpath element
                :param button_xpath: given button xpath
        """
        self.visibility_of_element_wait(self.driver, button_xpath)
        self.driver.find_element_by_xpath(button_xpath).click()

    def assert_if_element_is_visible(self, element_xpath):
        """Checks if web element is displayed
        :param element_xpath: element xpath to look for
        """
        self.assertTrue(self.driver.find_element_by_xpath(element_xpath), f'Element not found')

    def create_form_errors_number(self):
        error_field = self.driver.find_element_by_xpath(CL.error_alert_xpath).get_attribute("innerText")
        return error_field[10]

    def visibility_of_element_wait(self, driver, xpath, timeout=10) -> WebElement:
        """Check if element specified by xpath is visible on page
                  :param driver: webdriver or event firing webdriver instance
                  :param xpath:  web element xpath
                  :param timeout: after timeout waiting will be stopped (default: 10)
                  :return found element
        """
        locator = (By.XPATH, xpath)
        element_located = EC.presence_of_element_located(locator)

        if hasattr(driver, 'wrapped_driver'):
            unwrapped_driver = driver.wrapped_driver
            wait = WebDriverWait(unwrapped_driver, timeout)
        else:
            wait = WebDriverWait(driver, timeout)
        return wait.until(element_located, f"Element for xpath: '{xpath}'and url: {driver.current_url} not found")


class BaseTestClassUnits(BaseTestClass):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.authentication_page = page_factory.authentication_page(self.driver)
        self.home_page = page_factory.home_page(self.driver)
        print('Unit driver initialized')

    def tearDown(self):
        self.driver.quit()
        print('Unit driver finished')
