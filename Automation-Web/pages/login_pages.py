from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/register"
        self.FIRST_NAME_INPUT = (By.ID, "firstname")
        self.LAST_NAME_INPUT = (By.ID, "lastname")
        self.USERNAME_INPUT = (By.ID, "userName")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.REGISTER_BUTTON = (By.ID, "register")
        self.RECAPTCHA_IFRAME = (By.XPATH, "//iframe[contains(@title,'reCAPTCHA')]")

    def navigate(self, url=None):
        self.driver.get(url or self.url)

    def fill_form(self, first_name, last_name, username, password):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_register(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def wait_for_captcha(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.RECAPTCHA_IFRAME)
        )


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/login"
        self.USER_NAME_INPUT = (By.ID, "userName")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login")
        self.USER_NAME_VALUE = (By.ID, "userName-value")

    def navigate(self, url=None):
        self.driver.get(url or self.url)

    def fill_login(self, user_name, password):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys(user_name)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_output_text(self):
        return self.driver.find_element(*self.USER_NAME_VALUE).text
