import unittest
from tests.pages.test_authentication_page import AuthenticationPageSmokeTests
from tests.pages.test_create_account_page import CreateAccountPageSmokeTests
from tests.pages.test_home_page import HomePageTests


def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(HomePageTests))
    test_suite.addTest(unittest.makeSuite(AuthenticationPageSmokeTests))
    test_suite.addTest(unittest.makeSuite(CreateAccountPageSmokeTests))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())
