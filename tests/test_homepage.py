import time
from selenium.webdriver.common.by import By
from pages.signup_page import SignupPage
from data import signup_data
from pages.verify_email_page import VerifyEmailPage

def test_open_website(driver):

    driver.get("https://start-wise.io")

    time.sleep(1)

    essentials_button = driver.find_element(
        By.XPATH,
        "//button[text()='Essentials only']"
    )
    essentials_button.click()

    time.sleep(2)

    login_button = driver.find_element(
        By.XPATH,
        "//a[@href='/login']"
    )
    login_button.click()

    time.sleep(2)

    signup_button = driver.find_element(
        By.XPATH,
        "//button[contains(@class,'text-primary') and normalize-space()='Sign up']"
    )
    signup_button.click()

    time.sleep(1)

    signup_page = SignupPage(driver)


    # Insert email
    driver.find_element(
        *signup_page.EMAIL_FIELD
    ).send_keys(signup_data.EMAIL)


    # Verify email inserted
    assert signup_page.get_email_value() == signup_data.EMAIL


    # Insert full name
    driver.find_element(
        *signup_page.FULL_NAME_FIELD
    ).send_keys(signup_data.FULL_NAME)


    # Verify full name inserted
    assert signup_page.get_full_name_value() == signup_data.FULL_NAME

    # Insert password
    driver.find_element(
    *signup_page.PASSWORD_FIELD
    ).send_keys(signup_data.PASSWORD)

    # Verify password inserted
    assert signup_page.get_password_value() == signup_data.PASSWORD

    # Insert confirm password
    driver.find_element(
        *signup_page.CONFIRM_PASSWORD_FIELD
    ).send_keys(signup_data.CONFIRM_PASSWORD)

    # Verify confirm password inserted
    assert signup_page.get_confirm_password_value() == signup_data.CONFIRM_PASSWORD
    # Verify confirm password inserted
    assert signup_page.get_confirm_password_value() == signup_data.CONFIRM_PASSWORD
    signup_page.click_join_now()
    verify_email = VerifyEmailPage(driver)
    assert verify_email.verify_email_page_displayed(), \
    "Verify email page is not displayed"


    time.sleep(20)