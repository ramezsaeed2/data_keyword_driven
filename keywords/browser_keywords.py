def open_browser(driver, url):
    driver.get(url)

def enter_text(driver, locator, value):
    driver.find_element(*locator).send_keys(value)

def click_element(driver, locator):
    driver.find_element(*locator).click()

def verify_element_present(driver, locator):
    try:
        driver.find_element(*locator)
        return True
    except:
        return False
