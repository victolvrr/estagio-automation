from selenium.webdriver.common.by import By
import time
from pages import test_box_page

class TestTextBox:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        # Locators
        self.FULL_NAME_INPUT = (By.ID, "userName")
        self.EMAIL_INPUT = (By.ID, "userEmail")
        self.CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
        self.PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
        self.SUBMIT_BUTTON = (By.ID, "submit")
        self.OUTPUT_DIV = (By.ID, "output")

def test_fill_text_box_form_and_validate(driver):
    text_box_page = text_box_page.TextBoxPage(driver)

    text_box_page.navigate()
    # Test data for the form
    full_name = "Victor"
    email = "victor@gmail.com"
    current_address = "Rua do Bom Jesus, 123"
    permanent_address = "Avenida Conde da Boa Vista, 456"

    text_box_page.fill_form()
    text_box_page.submit()  

    output = text_box_page.get_output_text()

    assert full_name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output

