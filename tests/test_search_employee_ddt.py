import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.search_employee_page import SearchEmployeePage
from utils.read_data import get_csv_data
from selenium.common.exceptions import TimeoutException

@pytest.mark.parametrize("data", get_csv_data("data/search_employee_data.csv"))
def test_search_employee(data, driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login first
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    # Search Employee
    search = SearchEmployeePage(driver)
    search.navigate_to_search()
    search.search_employee(data["employee_name"])

    if data["expected_status"] == "success":
        assert search.is_employee_in_results(data["employee_name"])
    elif data["expected_status"] == "failure":
        assert search.is_no_records_found_message_displayed(data["expected_message"])