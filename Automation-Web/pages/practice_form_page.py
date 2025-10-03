from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.gender_radio = (By.XPATH, "//label[text()='{}']")
        self.mobile_input = (By.ID, "userNumber")
        self.dob_input = (By.ID, "dateOfBirthInput")
        self.subjects_input = (By.ID, "subjectsInput")
        self.hobbies_checkbox = (By.XPATH, "//label[text()='{}']")
        self.picture_upload = (By.ID, "uploadPicture")
        self.address_textarea = (By.ID, "currentAddress")
        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")
        self.submit_button = (By.ID, "submit")
        self.out_put_modal = (By.ID, "example-modal-sizes-title-lg")
        self.wait = (By.ID, "element_to_be_clickable")

    def navigate(self):
        self.driver.get(self.url)

    def fill_form(self, data):
        self.driver.find_element(*self.first_name_input).send_keys(data["first_name"])
        self.driver.find_element(*self.last_name_input).send_keys(data["last_name"])
        self.driver.find_element(*self.email_input).send_keys(data["email"])
        self.driver.find_element(By.XPATH, f"//label[text()='{data['gender']}']").click()
        self.driver.find_element(*self.mobile_input).send_keys(data["mobile"])
        # self.driver.execute_script("window.scrollBy(0, 300);")
        
        # Date of Birth
        dob_field = self.driver.find_element(*self.dob_input)
        dob_field.send_keys(Keys.CONTROL + "a")
        dob_field.send_keys(data["dob"])
        dob_field.send_keys(Keys.ENTER)

        # Subjects
        subjects_field = self.driver.find_element(*self.subjects_input)
        for subject in data["subjects"]:
            subjects_field.send_keys(subject)
            subjects_field.send_keys(Keys.ENTER)

        
        # State and City
        state_element = self.driver.find_element(*self.state_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_element)

        self.driver.find_element(*self.state_dropdown).click()
        self.driver.find_element(By.XPATH, f"//*[text()='{data['state']}']").click()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_element)
        self.driver.find_element(*self.city_dropdown).click()
        self.driver.find_element(By.XPATH, f"//*[text()='{data['city']}']").click()

        # Hobbies
        for hobby in data["hobbies"]:
            self.driver.find_element(By.XPATH, f"//label[text()='{hobby}']").click()

        # Picture
        # self.driver.find_element(*self.picture_upload).send_keys(data["picture"])

        self.driver.find_element(*self.address_textarea).send_keys(data["address"])


    def submit_form(self):
        button = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.find_element(*self.submit_button).click()

    def check_modal_visible(self):
        return self.driver.find_element(*self.out_put_modal).is_displayed()