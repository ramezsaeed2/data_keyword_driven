import csv
from keywords import browser_keywords as browser_kw
from keywords import validation_keywords as validation_kw

def test_failed_login_keyword_driven(driver):
    with open("data/failed_login.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            action = row["Action"]
            locator_type = row["LocatorType"]
            locator_value = row["LocatorValue"]
            test_data = row["TestData"]

            if action == "open_browser":
                browser_kw.open_browser(driver, locator_value)
            elif action == "input_text":
                browser_kw.input_text(driver, locator_type, locator_value, test_data)
            elif action == "click":
                browser_kw.click(driver, locator_type, locator_value)
            elif action == "verify_text":
                validation_kw.verify_element_text(driver, locator_type, locator_value, test_data)
            else:
                print(f"⚠️ Unknown action: {action}")