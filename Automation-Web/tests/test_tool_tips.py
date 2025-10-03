from pages.tool_tips_page import ToolTipsPage
import pytest
import json

@pytest.mark.widgets
def test_hover_over_button(driver, test_data):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])
    tool_tips_page.hover_over_button()
    text = tool_tips_page.get_tooltip_text()
    assert text == test_data["tool_tip_button_text"]

def test_hover_over_input(driver, test_data):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])
    tool_tips_page.hover_over_input()
    text = tool_tips_page.get_tooltip_text()
    assert text == test_data["tool_tip_field_text"]