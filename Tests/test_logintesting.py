import re
import allure
from playwright.sync_api import Page, expect
from Pages.firstPage import LoginPage
from Pages.homePage import HomePage
from Tests.BaseTest import BaseTest

class Tests(BaseTest):
    
    @allure.title("Successful login")
    def test_login(self, page):
        self.login(page)
        home = self.get_home(page)
        assert home.is_logged_in()
    
    @allure.title("Failed login")
    def test_failed_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("Admin", "Admin")
        assert login_page.is_error_appeared()
    
    @allure.title("Logout")
    def test_logout(self, page):
        self.login(page)
        home_page = self.get_home(page)
        home_page.logout()
        login_page = LoginPage(page)
        assert login_page.is_logged_out()
        
    @allure.title("Profile dropdown menu")
    def test_profile_dropdown(self, page):
        self.login(page)
        home_page = self.get_home(page)
        assert home_page.is_logged_in()
        home_page.is_everything_in_dropdown()
        home_page.logout()
    
