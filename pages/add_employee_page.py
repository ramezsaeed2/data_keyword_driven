from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.add_button = (By.XPATH, "//a[text()='Add Employee']")
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_add_employee(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def add_employee(self, first_name, last_name, valid="Success"):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.last_name)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
        if valid=="Success":
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]"))
            )

    def is_error_message_displayed(self, expected_message):
        # error_message_locator = (By.XPATH, f"//span[contains(@class, 'oxd-text--span') and contains(@class, 'oxd-input-field-error-message') and contains(text(), '{expected_message}')]")
        # self.error_message = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message') and text()='Required']")
        error_message_locator = (By.XPATH, f"//span[contains(@class, 'oxd-input-field-error-message') and text()='{expected_message}']")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(error_message_locator)
            )
            return True
        except:
            return False
