from pages.elementes_pages import ElementsPage
import pytest

@pytest.mark.smoke
def test_navigate_to_elements_page(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert "elements" in driver.current_url

@pytest.mark.smoke
def test_locate_by_id(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_checkbox_id_visible()
    assert elements_page.get_menu_checkbox_id_text() == "Text Box"

@pytest.mark.smoke
def test_locate_by_css_selector(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_checkbox_css_is_visible()

def test_locate_by_xpath(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()

    assert elements_page.is_checkbox_menu_xpath_visible()