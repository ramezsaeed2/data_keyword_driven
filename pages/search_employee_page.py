from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.employee_name_field = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
        self.search_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

    def search_employee(self, employee_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.employee_name_field)
        ).send_keys(employee_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']"))
        )

    def is_employee_in_results(self, employee_name):
        # Assuming employee name appears in a cell within the table body
        first_name, last_name = employee_name.split(" ", 1)
        first_name_locator = (By.XPATH, f"//div[@class='oxd-table-body']//div[contains(text(), '{first_name}')]")
        last_name_locator = (By.XPATH, f"//div[@class='oxd-table-body']//div[contains(text(), '{last_name}')]")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(first_name_locator)
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(last_name_locator)
            )
            return True
        except:
            return False

    def is_no_records_found_message_displayed(self, expected_message):
        no_records_locator = (By.XPATH, f"//span[text()='{expected_message}']")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(no_records_locator)
            )
            return True
        except:
            return False
