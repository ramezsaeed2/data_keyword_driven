import pytest
import os
from pages.login_page import LoginPage
from utils.read_data import get_csv_data

@pytest.mark.parametrize("data", get_csv_data(os.path.join(os.path.dirname(__file__), "..", "data", "login_data.csv")))
def test_login(data, driver):
    login = LoginPage(driver)
    login.open()

    login.set_username(data['username'])
    login.set_password(data['password'])
    login.click_login()

    result = login.is_login_successful()

    if data['expected'] == 'Success':
        assert result, f"Expected success but got failure for {data['username']}"
        login.click_logout()
    else:
        assert not result, f"Expected failure but got success for {data['username']}"