from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import web_reader
from utils.inputs import Input
from utils.locators import AuthLocators
import time


class AuthenticationPage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web["authentication_url"]
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self

    def click_button(self, button_xpath):
        """Click button action on given xpath element
                :param button_xpath: given button xpath
                :return: self
        """
        button = self.visibility_of_element_wait(self.driver, button_xpath)
        button.click()
        return self

    def send_text_to_input_field(self, input_field_xpath, input_text):
        """Fill selected input field with given text
                :param input_field_xpath: given input field xpath
                :param input_text: text to fill with
                :return: self
        """
        input_field = self.driver.find_element_by_xpath(input_field_xpath)
        input_field.send_keys(input_text)
        return self

    def input_data_and_click(self, input_field_xpath, input_text, button):
        """Fill selected input field with given text and click the button
                :param input_field_xpath: given input field xpath
                :param input_text: text to fill with
                :param button: button xpath passed to click_button method
                :return: None
        """
        self.driver.find_element_by_xpath(input_field_xpath).clear()
        self.send_text_to_input_field(input_field_xpath, input_text)
        self.click_button(button)
        time.sleep(3)

    def visit_create_account_form(self):
        self.input_data_and_click(AuthLocators.email_input_field_xpath, Input.valid_email,
                                                AuthLocators.create_account_button)
        time.sleep(2)
        return self

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