from selenium.webdriver.common.by import By


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    FULL_NAME_FIELD = (By.XPATH, "//input[@id='full-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@id='confirm-password']")
    JOIN_NOW_BUTTON = (By.XPATH, "//button[normalize-space()='Join Now']")

    def get_email_value(self):
        return self.driver.find_element(
            *self.EMAIL_FIELD
        ).get_attribute("value")
# Verify full name value
    def get_full_name_value(self):
        return self.driver.find_element(
            *self.FULL_NAME_FIELD
        ).get_attribute("value")
    # Verify password value
    def get_password_value(self):
        return self.driver.find_element(
            *self.PASSWORD_FIELD
        ).get_attribute("value")
    # Verify confirm password value
    def get_confirm_password_value(self):
        return self.driver.find_element(
        *self.CONFIRM_PASSWORD_FIELD
        ).get_attribute("value") 
    def click_join_now(self):
        self.driver.find_element(
        *self.JOIN_NOW_BUTTON
        ).click()   