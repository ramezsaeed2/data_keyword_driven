import pytest
from pages.login_page import LoginPage
from pages.add_employee_page import AddEmployeePage
from utils.read_data import get_csv_data
from selenium.common.exceptions import TimeoutException

@pytest.mark.parametrize("data", get_csv_data("data/add_employee_data.csv"))
def test_add_employee(data, driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login first
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    # Add Employee
    add = AddEmployeePage(driver)
    add.navigate_to_add_employee()
    add.add_employee(data["first_name"], data["last_name"], valid=data["expected_status"])

    if data["expected_status"] == "success":
        # The AddEmployeePage already waits for the success message.
        # If the success message is not found, a TimeoutException will be raised, failing the test.
        pass
    elif data["expected_status"] == "failure":
        assert add.is_error_message_displayed(data["expected_message"])
