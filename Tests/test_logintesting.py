import re
import allure
from playwright.sync_api import Page, expect
from Pages.firstPage import LoginPage
from Pages.homePage import HomePage


@allure.title("Successful login")
def test_login(page):
    login = LoginPage(page)
    home_page = HomePage(page)
    username = "Admin"
    password = "admin123"
    login.open_login_page()
    login.login(username, password)  # Демонстрационные данные
    assert home_page.is_logged_in()
    
@allure.title("Failed login")
def test_failed_login(page):
    username = "Admin"
    password = "Admin"
    login = LoginPage(page)
    login.open_login_page()
    login.login(username, password)
    assert login.is_error_appeared()
    
@allure.title("Logout")
def test_logout(page):
    username = "Admin"
    password = "admin123"
    login = LoginPage(page)
    home_page = HomePage(page)
    login.open_login_page()
    login.login(username, password)
    home_page.logout()
    assert login.is_logged_out()
    
