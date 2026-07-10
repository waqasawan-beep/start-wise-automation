import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from data import login_data


def test_login(driver):

    driver.get("https://start-wise.io")

    time.sleep(2)

    # Accept cookies
    essentials_button = driver.find_element(
        By.XPATH,
        "//button[text()='Essentials only']"
    )
    essentials_button.click()

    time.sleep(2)

    # Click login
    login_button = driver.find_element(
        By.XPATH,
        "//a[@href='/login']"
    )
    login_button.click()

    time.sleep(3)

    login_page = LoginPage(driver)

    # Insert email
    driver.find_element(
        *login_page.EMAIL_FIELD
    ).send_keys(login_data.EMAIL)

    # Verify email inserted
    assert login_page.get_email_value() == login_data.EMAIL

      # Insert password
    driver.find_element(
        *login_page.PASSWORD_FIELD
    ).send_keys(login_data.PASSWORD)


    # Verify password inserted
    assert login_page.get_password_value() == login_data.PASSWORD
    login_page.click_signin()

    time.sleep(5)
    # Verify dashboard opened
    assert login_page.is_dashboard_displayed(), \
    "Dashboard is not displayed after successful login"

