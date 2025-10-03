from pages.alert_pages import HomePage, AlertsFramesWindowsPage, AlertsPage
import pytest

@pytest.fixture(scope="function")
def setup_alerts_page(driver):
    home_page = HomePage(driver)
    home_page.navigate()
    # CORREÇÃO: Removido o 's' extra de 'alerts' para corresponder ao nome do método
    home_page.click_alert_frame_windows_card() 
    
    alerts_frames_windows_page = AlertsFramesWindowsPage(driver)
    alerts_frames_windows_page.click_alerts_menu_item()
    
    return AlertsPage(driver)

@pytest.mark.alerts
def test_simple_alert(setup_alerts_page):
    alerts_page = setup_alerts_page
    alerts_page.click_button_alert()
    alerts_page.accept_alert()

@pytest.mark.alerts
def test_timer_alert(setup_alerts_page):
    alerts_page = setup_alerts_page
    alerts_page.click_button_timer_alert()
    alerts_page.accept_alert()

@pytest.mark.alerts
def test_confirm_alert_accept(setup_alerts_page):
    alerts_page = setup_alerts_page
    alerts_page.click_button_confirm()
    alerts_page.accept_alert()
    assert "You selected Ok" in alerts_page.get_confirm_result_text()

@pytest.mark.alerts
def test_confirm_alert_dismiss(setup_alerts_page):
    alerts_page = setup_alerts_page
    alerts_page.click_button_confirm()
    alerts_page.dismiss_alert()
    assert "You selected Cancel" in alerts_page.get_confirm_result_text()

@pytest.mark.alerts
def test_prompt_alert_accept(setup_alerts_page):
    alerts_page = setup_alerts_page
    alerts_page.click_button_prompt()
    alerts_page.send_keys_to_alert("Testando Prompt")
    assert "You entered Testando Prompt" in alerts_page.get_prompt_result_text()

@pytest.mark.alerts
def test_prompt_alert_dismiss(setup_alerts_page):
    alerts_page = setup_alerts_page
    alerts_page.click_button_prompt()
    alerts_page.dismiss_alert()
    assert "You entered" not in alerts_page.get_prompt_result_text()

