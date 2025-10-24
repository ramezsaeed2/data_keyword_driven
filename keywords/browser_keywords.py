from utils.locator_helper import get_locator

def open_browser(driver, url):
    driver.get(url)

def input_text(driver, locator_type, locator_value, test_data):
    locator = get_locator(locator_type, locator_value)
    element = driver.find_element(*locator)
    element.clear()
    element.send_keys(test_data)

def click(driver, locator_type, locator_value):
    locator = get_locator(locator_type, locator_value)
    driver.find_element(*locator).click()

def verify_text(driver, locator_type, locator_value, expected_text):
    locator = get_locator(locator_type, locator_value)
    element = driver.find_element(*locator)
    actual_text = element.text
    assert expected_text in actual_text, f"Expected '{expected_text}', got '{actual_text}'"
