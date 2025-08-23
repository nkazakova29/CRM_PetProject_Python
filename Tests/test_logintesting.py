import re
from playwright.sync_api import Page, expect
from Pages.firstPage import LoginPage

def test_login(page):
    login = LoginPage(page)
    login.open()
    login.open_login_page()
    login.login("will", "will")  # Демонстрационные данные
    login.time_zone_chosing()
    assert login.is_logged_in()
    
