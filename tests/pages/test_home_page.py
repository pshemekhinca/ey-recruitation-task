from tests.pages.base_test_class import BaseTestClass
from utils.locators import HomeLocators


class HomePageTests(BaseTestClass):

    def test_home_page_title_TC_001(self):
        expected_title = "My Store"
        self.home_page.visit()
        self.assertEqual(expected_title, self.driver.title,
                         f'Expected title differ from the {self.driver.current_url} title page')

    def test_signin_button_is_displayed_TC_002(self):
        self.home_page.visit()
        self.visibility_of_element_wait(self.driver, HomeLocators.signin_button_xpath)

    def test_correct_redirection_after_signin_button_click_TC_003(self):
        expected_header_text = "AUTHENTICATION"
        self.home_page.visit()
        self.click_button(HomeLocators.signin_button_xpath)
        header = self.driver.find_element_by_xpath(HomeLocators.page_header_xpath)
        self.assertEqual(expected_header_text, header.text,
                         f'Expected header text differ from the {self.driver.current_url} header')
