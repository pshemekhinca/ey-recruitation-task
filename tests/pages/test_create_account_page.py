from selenium.webdriver.support.select import Select
import re
from tests.pages.base_test_class import *
from utils import web_reader
from utils.locators import CreateLocators as CL
from utils.inputs import Input
import time


class CreateAccountPageTests(BaseTestClass):

    def go_to_create_account_form(self):
        web = web_reader.load()
        create_for_urls = [web["create_error_url"], web["create_account_url"], web["create_back_url"]]
        if self.driver.current_url not in create_for_urls:
            self.authentication_page.visit()
            self.authentication_page.visit_create_account_form()
            time.sleep(3)
        else:
            return self

    def radio_button_status(self, button_xpath):
        """Click button action on given xpath element
                :param button_xpath: given radio button xpath
                :return: button_status True/False
        """
        self.click_button(button_xpath)
        time.sleep(1)
        return self.driver.find_element_by_xpath(button_xpath).is_selected()

    def invalid_input_length_error(self, field_xpath, text_input, button_xpath, error_xpath):
        """Invalid values input steps to check if length limits returns error
                :param field_xpath: given field xpath
                :param text_input: given text
                :param button_xpath: button xpath to be clicked
                :return: error_xpath: returns error message to verify with the expected one
        """
        self.go_to_create_account_form()
        self.authentication_page.input_data_and_click(field_xpath, text_input,
                                                      button_xpath)
        return self.visibility_of_element_wait(self.driver, error_xpath)

    def errors_number_before_and_after(self, button_xpath, field_xpath, text_input):
        self.click_button(button_xpath)
        time.sleep(1)
        start_error_number = self.create_form_errors_number()
        # self.authentication_page.send_text_to_input_field(field_xpath, text_input)
        # self.click_button(button_xpath)
        self.authentication_page.input_data_and_click(field_xpath, text_input,button_xpath)
        time.sleep(1)
        end_error_number = self.create_form_errors_number()
        return f'{start_error_number}_{end_error_number}'


class CreateAccountPageSmokeTests(CreateAccountPageTests):
    def test_required_create_account_form_fields_are_displayed_on_page_TC_010(self):
        self.go_to_create_account_form()
        for field in CL.required_fields:
            with self.subTest(field):
                self.visibility_of_element_wait(self.driver, field)

    def test_register_button_is_displayed_on_page_TC_011(self):
        self.go_to_create_account_form()
        self.visibility_of_element_wait(self.driver, CL.register_button_xpath)

    def test_auto_completed_email_field_value_TC_012(self):
        expected_email_value = Input.valid_email
        self.go_to_create_account_form()
        email_value = self.driver.find_element_by_xpath(CL.email_rq_xpath).get_attribute('defaultValue')
        self.assertEqual(expected_email_value, email_value, f'Expected email field value differ from {email_value}')

    def test_country_default_value_selected_TC_013(self):
        expected_country_value = 'United States'
        self.go_to_create_account_form()
        country_value = self.driver.find_element_by_xpath(CL.country_rq_select_xpath)
        self.assertIn(expected_country_value, country_value.text,
                      f'Expected country preselected value differ from {country_value.text}')


class CreateAccountPageSanityTests(CreateAccountPageTests):

    def test_error_message_after_submit_default_values_and_empty_fields_TC_014(self):
        expected_error_message = 'There are 8 errors'
        self.go_to_create_account_form()
        self.click_button(CL.register_button_xpath)
        time.sleep(1)
        error_field = self.driver.find_element_by_xpath(CL.error_alert_xpath).get_attribute("innerText")
        actual_error = (error_field.split(' \n', 1)[0])
        self.assertIn(expected_error_message, actual_error,
                      f'Expected error text differ from {actual_error}')

    def test_first_name_input_result_sets_given_name_copy_in_address_section_TC_015(self):
        expected_name = Input.valid_first_name
        self.go_to_create_account_form()
        self.authentication_page.send_text_to_input_field(CL.first_name_rq_xpath, expected_name)
        actual_name_value = self.driver.find_element_by_xpath(CL.first_name_auto_xpath).get_attribute('value')
        self.assertEqual(expected_name, actual_name_value,
                         f'Expected email field value differ from {actual_name_value}')

    def test_last_name_input_result_sets_given_name_copy_in_address_section_TC_016(self):
        expected_last_name = Input.valid_last_name
        self.go_to_create_account_form()
        self.authentication_page.send_text_to_input_field(CL.last_name_rq_xpath, expected_last_name)
        actual_last_name_value = self.driver.find_element_by_xpath(CL.last_name_auto_xpath).get_attribute('value')
        self.assertEqual(expected_last_name, actual_last_name_value,
                         f'Expected email field value differ from {actual_last_name_value}')

    def test_errors_number_decrease_after_each_input_into_required_field_TC_017(self):
        self.go_to_create_account_form()
        error_number = self.errors_number_before_and_after(CL.register_button_xpath, CL.city_rq_xpath,
                                                           Input.valid_city)
        self.assertGreater(error_number[0], error_number[2],
                           f'Errors number is not decreasing with required data input')

    def test_errors_number_increase_after_required_field_data_cleared_TC_018(self):
        self.go_to_create_account_form()
        self.click_button(CL.register_button_xpath)
        time.sleep(1)
        start_error_number = self.create_form_errors_number()
        self.driver.find_element_by_xpath(CL.email_rq_xpath).clear()
        self.click_button(CL.register_button_xpath)
        end_error_number = self.create_form_errors_number()
        time.sleep(1)
        self.assertLess(start_error_number, end_error_number,
                        f'Errors number is not decreasing with required data input')


class CreateAccountFormValidRegistration(CreateAccountPageTests):

    def test_mr_of_radio_buttons_can_be_selected_TC_019(self):
        self.go_to_create_account_form()
        mr_radio_button = self.radio_button_status(CL.mr_radio_xpath)
        self.assertEqual(mr_radio_button, True, 'The radio button is not selected')

    def test_if_mrs_radio_button_select_switch_off_mr_radio_button_TC_020(self):
        self.go_to_create_account_form()
        mrs_radio_button = self.radio_button_status(CL.mrs_radio_xpath)
        mr_radio_button = self.driver.find_element_by_xpath(CL.mr_radio_xpath).is_selected()
        self.assertEqual(mrs_radio_button, True, 'Mrs radio button is not selected')
        self.assertNotEqual(mrs_radio_button, mr_radio_button, "Mrs radio button not correctly selected")

    def test_error_message_after_submit_incorrect_first_name_format_TC_021(self):
        expected_error_message = 'firstname is invalid.'
        self.go_to_create_account_form()
        self.click_button(CL.register_button_xpath)
        time.sleep(1)
        for entry in Input.incorrect_first_name:
            with self.subTest(entry):
                self.authentication_page.input_data_and_click(CL.first_name_rq_xpath, entry,
                                                              CL.register_button_xpath)
                time.sleep(2)
                actual_error = self.visibility_of_element_wait(self.driver, CL.error_alert_xpath)
                self.assertIn(expected_error_message, actual_error.text,
                              f'Expected error text differ from {actual_error}')

    def test_error_message_after_submit_incorrect_last_name_format_TC_022(self):
        expected_error_message = 'lastname is invalid.'
        self.go_to_create_account_form()
        self.click_button(CL.register_button_xpath)
        time.sleep(1)
        for entry in Input.incorrect_first_name:
            with self.subTest(entry):
                self.authentication_page.input_data_and_click(CL.last_name_rq_xpath, entry,
                                                              CL.register_button_xpath)
                time.sleep(2)
                actual_error = self.visibility_of_element_wait(self.driver, CL.error_alert_xpath)
                self.assertIn(expected_error_message, actual_error.text,
                              f'Expected error text differ from {actual_error}')

    def test_first_name_length_can_consist_of_more_than_32_letters_TC_023(self):
        expected_error_message = 'firstname is too long.'
        actual_error = self.invalid_input_length_error(CL.first_name_rq_xpath, Input.long_name,
                                                       CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_last_name_length_can_consist_of_more_than_32_letters_TC_024(self):
        expected_error_message = 'lastname is too long.'
        actual_error = self.invalid_input_length_error(CL.last_name_rq_xpath, Input.long_name, CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_password_length_can_consist_of_more_than_32_letters_TC_025(self):
        expected_error_message = 'passwd is too long.'
        actual_error = self.invalid_input_length_error(CL.password_rq_xpath, Input.long_name, CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_password_length_can_be_shorter_than_5_letters_TC_026(self):
        expected_error_message = 'passwd is invalid.'
        actual_error = self.invalid_input_length_error(CL.password_rq_xpath, Input.short_input,
                                                       CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_city_field_can_be_filled_with_over_64_characters_name_TC_027(self):
        expected_error_message = 'city is too long'
        actual_error = self.invalid_input_length_error(CL.city_rq_xpath, Input.very_long_name, CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_error_after_zip_code_field_input_with_alpha_numeric_characters_TC_028(self):
        expected_error_message = "The Zip/Postal code you've entered is invalid"
        actual_error = self.invalid_input_length_error(CL.zip_rq_xpath, Input.invalid_zip_code,
                                                       CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_errors_number_decrease_after_valid_zip_code_submitted_TC_029(self):
        self.go_to_create_account_form()
        error_number = self.errors_number_before_and_after(CL.register_button_xpath, CL.zip_rq_xpath,
                                                           Input.valid_zip_code)
        print(error_number)
        self.assertGreater(error_number[0], error_number[2],
                           f'Errors number is not decreasing with required data input')

    def test_error_after_zip_code_field_input_with_alpha_numeric_characters_TC_030(self):
        expected_error_message = "phone_mobile is invalid"
        actual_error = self.invalid_input_length_error(CL.mobile_rq_xpath, Input.invalid_mobile_no,
                                                       CL.register_button_xpath,
                                                       CL.error_alert_xpath)
        self.assertIn(expected_error_message, actual_error.text,
                      f'Expected error text differ from {actual_error}')

    def test_errors_number_decrease_after_valid_mobile_phone_number_submitted_TC_031(self):
        self.go_to_create_account_form()
        error_number = self.errors_number_before_and_after(CL.register_button_xpath, CL.mobile_rq_xpath,
                                                           Input.valid_mobile_no)
        print(error_number)
        self.assertGreater(error_number[0], error_number[2],
                           f'Errors number is not decreasing with required data input')


class CreateAccountSuccess(BaseTestClassUnits, CreateAccountPageTests):
    def test_success_account_creation_with_required_fields_only(self):
        self.go_to_create_account_form()
        for field, value in CL.required_fields.items():
            if re.compile('state').findall(field):
                select = Select(self.driver.find_element_by_xpath(field))
                select.select_by_value(value)
            else:
                self.authentication_page.send_text_to_input_field(field, value)
        self.click_button(CL.register_button_xpath)
        success_header = self.visibility_of_element_wait(self.driver, CL.my_account_header)
        self.assertEqual('MY ACCOUNT', success_header.text, 'Account creation not succeed')



