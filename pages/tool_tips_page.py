from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ToolTipsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/tool-tips"
        self.wait = WebDriverWait(self.driver, 10)
        # Locators
        self.BUTTON_HOVER = (By.ID, "toolTipButton")
        self.INPUT_HOVER = (By.ID, "toolTipTextField")
        self.TOOL_TIP_MESSAGE = (By.CSS_SELECTOR, ".tooltip-inner")

    def navigate(self, url):
        self.driver.get(url)

    def hover_over_button(self):
        button = self.driver.find_element(*self.BUTTON_HOVER)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        webdriver.ActionChains(self.driver).move_to_element(button).perform()

    def hover_over_input(self):
        input_field = self.driver.find_element(*self.INPUT_HOVER)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", input_field)
        webdriver.ActionChains(self.driver).move_to_element(input_field).perform()

    def get_tooltip_text(self):
        tooltip = self.wait.until(EC.visibility_of_element_located(self.TOOL_TIP_MESSAGE))
        return tooltip.text