from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SIGNIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    DASHBOARD_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='AI Venture Tools']"
    )


    def __init__(self, driver):
        self.driver = driver


    def get_email_value(self):
        return self.driver.find_element(
            *self.EMAIL_FIELD
        ).get_attribute("value")


    def get_password_value(self):
        return self.driver.find_element(
            *self.PASSWORD_FIELD
        ).get_attribute("value")


    def click_signin(self):
        self.driver.find_element(
            *self.SIGNIN_BUTTON
        ).click()


    def is_dashboard_displayed(self):

        try:
            return self.driver.find_element(
                *self.DASHBOARD_TITLE
            ).is_displayed()

        except NoSuchElementException:
            return False