import csv
from keywords import browser_keywords as kw

def test_keyword_driven(driver):

    with open("data/login_keywords.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            action = row["Action"]
            locator_type = row["LocatorType"]
            locator_value = row["LocatorValue"]
            test_data = row["TestData"]

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

