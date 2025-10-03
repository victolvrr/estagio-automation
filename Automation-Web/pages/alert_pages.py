from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com"
        self.wait = WebDriverWait(self.driver, 10 )
        self.alerts_frames_windows_card = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")

    def navigate(self):
        self.driver.get(self.url)
    
    def click_alert_frame_windows_card(self):
        element = self.driver.find_element(*self.alerts_frames_windows_card)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

class AlertsFramesWindowsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/alertsWindows"
        self.alerts_menu_item = (By.XPATH, "//span[text( )='Alerts']")

    def navigate(self):
        self.driver.get(self.url)

    def click_alerts_menu_item(self):
        element = self.driver.find_element(*self.alerts_menu_item)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/alerts"
        self.button_alert = (By.ID, "alertButton" )
        self.button_timer_alert = (By.ID, "timerAlertButton")
        self.button_confirm = (By.ID, "confirmButton")
        self.button_prompt = (By.ID, "promtButton")
        self.confirm_result = (By.ID, "confirmResult")
        self.prompt_result = (By.ID, "promptResult")

    def navigate(self):
        self.driver.get(self.url)

    # Métodos para clicar
    def click_button_alert(self):
        self.driver.find_element(*self.button_alert).click()

    def click_button_timer_alert(self):
        self.driver.find_element(*self.button_timer_alert).click()

    def click_button_confirm(self):
        self.driver.find_element(*self.button_confirm).click()

    def click_button_prompt(self):
        self.driver.find_element(*self.button_prompt).click()

    # Métodos para lidar com alerts
    def accept_alert(self):
        # Adicionando espera explícita para o alerta aparecer
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def send_keys_to_alert(self, text):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def get_confirm_result_text(self):
        return self.driver.find_element(*self.confirm_result).text

    def get_prompt_result_text(self):
        return self.driver.find_element(*self.prompt_result).text
