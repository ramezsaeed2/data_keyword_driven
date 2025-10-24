from utils.locator_helper import get_locator

def verify_element_text(driver, locator_type, locator_value, expected_text):
    locator = get_locator(locator_type, locator_value)
    element = driver.find_element(*locator)
    actual_text = element.text
    assert expected_text in actual_text, f"Expected '{expected_text}', but found '{actual_text}'"

def verify_element_present(driver, locator_type, locator_value):
    locator = get_locator(locator_type, locator_value)
    assert driver.find_elements(*locator), f"Element with locator type '{locator_type}' and value '{locator_value}' not found."