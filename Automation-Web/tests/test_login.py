import pytest
import time
from pages.login_pages import LoginPage, RegisterPage


def test_register_and_login(driver):
    register_page = RegisterPage(driver)
    register_page.navigate()

    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*register_page.REGISTER_BUTTON))
    first_name = "Victor"
    last_name = "Oliveira"
    user_name = "victolvrr"
    password = "Victor123!"
    register_page.fill_form(first_name, last_name, user_name, password)

    time.sleep(15)
    register_page.wait_for_captcha()
    register_page.click_register()

    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.fill_login(user_name, password)
    login_page.submit()
