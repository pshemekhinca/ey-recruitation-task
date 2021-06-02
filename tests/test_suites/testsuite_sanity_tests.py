import unittest
from tests.pages.test_authentication_page import AuthenticationPageSanityTests
from tests.pages.test_create_account_page import CreateAccountPageSanityTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AuthenticationPageSanityTests))
    test_suite.addTest(unittest.makeSuite(CreateAccountPageSanityTests))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sanity_suite())
