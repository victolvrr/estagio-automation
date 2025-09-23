from selenium.webdriver.common.by import By

class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/checkbox"
        # Locators
        self.EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.NOTES_CHECKBOX_LABEL = (By.XPATH, "//label[@for='tree-node-notes']")
        self.label_notes = (By.XPATH, "//label[@for='tree-node-notes']")
        self.NOTES_INPUT = (By.ID, "tree-node-notes")

    def navigate(self):
        self.driver.get(self.url)

    def expand_all(self):
        self.driver.find_element(*self.EXPAND_ALL_BUTTON).click()

    def select_notes(self):
        self.driver.find_element(*self.NOTES_CHECKBOX_LABEL).click()

    def is_notes_selected(self):
        return self.driver.find_element(*self.NOTES_INPUT).is_selected()


# Teste com pytest
def test_checkbox(driver):
    checkbox_page = CheckBoxPage(driver)
    checkbox_page.navigate()
    checkbox_page.expand_all()
    checkbox_page.select_notes()

    assert checkbox_page.is_notes_selected()
