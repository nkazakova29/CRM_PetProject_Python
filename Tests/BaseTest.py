import re
from playwright.sync_api import Page, expect
from Pages.firstPage import LoginPage
from Pages.homePage import HomePage

class BaseTest:
    username = "Admin"
    password = "admin123"
    def login(self, page: Page, username: str = None, password: str = None):
        login = LoginPage(page)
        login.open()
        login.login(username or self.username, password or self.password)
        return login
    
    def get_home(self, page):
        return HomePage(page)
