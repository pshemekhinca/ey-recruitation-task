from utils import web_reader


class CreateAccountPage:
    def __init__(self, driver):
        web = web_reader.load()
        self.driver = driver
        self.driver.get(web["authentication_url"])




