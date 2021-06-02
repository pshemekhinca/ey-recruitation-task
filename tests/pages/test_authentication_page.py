from tests.pages.base_test_class import *
from utils.locators import AuthLocators, CreateLocators
from utils.inputs import Input
import time


class AuthenticationPageSmokeTests(BaseTestClass):

    def test_create_account_form_is_displayed_on_authentication_page_TC_004(self):
        self.authentication_page.visit()
        self.visibility_of_element_wait(self.driver, AuthLocators.form_section_xpath)

    def test_email_input_field_is_displayed_on_authentication_page_TC_005(self):
        self.authentication_page.visit()
        self.visibility_of_element_wait(self.driver, AuthLocators.email_input_field_xpath)

    def test_create_account_button_is_displayed_on_authentication_page_TC_006(self):
        self.authentication_page.visit()
        self.visibility_of_element_wait(self.driver, AuthLocators.create_account_button)

    # alternative for separate TC_004-TC_006, could be web elements display test in one turn
    def test_authentication_form_elements_are_displayed(self):
        web_elements_list = [AuthLocators.form_section_xpath,
                             AuthLocators.email_input_field_xpath,
                             AuthLocators.create_account_button]
        self.authentication_page.visit()
        for web_element in web_elements_list:
            with self.subTest(web_element):
                self.visibility_of_element_wait(self.driver, web_element)


class AuthenticationPageSanityTests(BaseTestClassUnits):

    def test_error_message_after_blank_email_field_submitted_TC_007(self):
        expected_error_message = 'Invalid email address.'
        self.authentication_page.visit()
        self.authentication_page.input_data_and_click(AuthLocators.email_input_field_xpath, '',
                                                      AuthLocators.create_account_button)
        time.sleep(2)
        actual_error_text = self.get_element_text_value(AuthLocators.error_message_xpath)
        self.assertIn(expected_error_message, actual_error_text,
                         f'Expected error message differ from {actual_error_text}')

    def test_error_message_after_several_invalid_emails_submitted_TC_008(self):
        expected_error_message = 'Invalid email address.'
        self.authentication_page.visit()
        for entry in Input.invalid_email:
            with self.subTest(entry):
                self.authentication_page.input_data_and_click(AuthLocators.email_input_field_xpath, entry,
                                                              AuthLocators.create_account_button)
                actual_error = self.visibility_of_element_wait(self.driver, AuthLocators.error_message_xpath)
                self.assertEqual(expected_error_message, actual_error.text,
                                 f'Expected error message differ from {actual_error.text}')

    def test_correct_redirection_after_valid_email_submitted_TC_009(self):
        self.authentication_page.visit()
        self.authentication_page.input_data_and_click(AuthLocators.email_input_field_xpath, Input.valid_email,
                                                      AuthLocators.create_account_button)
        self.visibility_of_element_wait(self.driver, CreateLocators.create_account_form_xpath)
