import unittest

from tests.pages.test_authentication_page import AuthenticationPageSmokeTests, AuthenticationPageSanityTests
from tests.pages.test_create_account_page import CreateAccountPageSmokeTests, CreateAccountPageSanityTests, \
    CreateAccountFormValidRegistration, CreateAccountSuccess
from tests.pages.test_home_page import HomePageTests


def all_tests_suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(HomePageTests))
    test_suite.addTest(unittest.makeSuite(AuthenticationPageSmokeTests))
    test_suite.addTest(unittest.makeSuite(AuthenticationPageSanityTests))
    test_suite.addTest(unittest.makeSuite(CreateAccountPageSmokeTests))
    test_suite.addTest(unittest.makeSuite(CreateAccountPageSanityTests))
    test_suite.addTest(unittest.makeSuite(CreateAccountFormValidRegistration))
    test_suite.addTest(unittest.makeSuite(CreateAccountSuccess))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(all_tests_suite())
