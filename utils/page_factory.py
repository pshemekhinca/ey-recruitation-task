from src.pages.authentication_page import AuthenticationPage
from src.pages.home_page import HomePage
# from src.pages.create_account_page import CreateAccountPage


def authentication_page(driver):
    return AuthenticationPage(driver)


def home_page(driver):
    return HomePage(driver)


# def create_account_page(driver):
#     return CreateAccountPage(driver)
