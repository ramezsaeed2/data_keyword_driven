from selenium.webdriver.common.by import By

def get_locator(locator_type, locator_value):
    locator_type = locator_type.lower()
    if locator_type == "id":
        return (By.ID, locator_value)
    elif locator_type == "name":
        return (By.NAME, locator_value)
    elif locator_type == "xpath":
        return (By.XPATH, locator_value)
    elif locator_type == "css":
        return (By.CSS_SELECTOR, locator_value)
    elif locator_type == "link":
        return (By.LINK_TEXT, locator_value)
    else:
        raise ValueError(f"Unsupported locator type: {locator_type}")
