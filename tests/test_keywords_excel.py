from keywords import browser_keywords as kw
from utils.excel_reader import read_excel_data

def test_keyword_driven_excel(driver):

    # Read Excel test steps
    test_steps = read_excel_data("data/login_keywords.xlsx", "LoginTest")

    for step in test_steps:
        action = step["Action"]
        locator_type = step["LocatorType"]
        locator_value = step["LocatorValue"]
        test_data = step["TestData"]

        if action == "open_browser":
            kw.open_browser(driver, locator_value)
        elif action == "input_text":
            kw.input_text(driver, locator_type, locator_value, test_data)
        elif action == "click":
            kw.click(driver, locator_type, locator_value)
        elif action == "verify_text":
            kw.verify_text(driver, locator_type, locator_value, test_data)
        else:
            print(f"⚠️ Unknown action: {action}")
