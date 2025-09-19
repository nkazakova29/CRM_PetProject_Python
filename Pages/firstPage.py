import allure
import allure
from playwright.sync_api import Page
from conftest import page

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/"
    
    def __init__(self, page: Page):
        self.page = page
        
    @allure.step("Open CRM website")
    def open_login_page(self):
        with allure.step("Open CRM site"):
            self.page.goto(self.URL)
        
    @allure.step("Sign in process")
    def login(self, username: str, password: str):
        with allure.step("Sign in process"):
            self.page.fill("[name='username']", username)
            self.page.fill("[name='password']", password)
            self.page.click("[type='submit']")
                    
    @allure.step("Checking if an login error has appeared")    
    def is_error_appeared(self):
        with allure.step("Checking if an authorization error has appeared"):
            try:
                self.page.wait_for_selector("text=Invalid credentials", timeout=5000)
                return True
            except:
                return False
    
    @allure.step("Checking if a user has been logged out")
    def is_logged_out(self):
        with allure.step("Checking if a user has been logged out"):
            try:
                self.page.wait_for_selector("[type='submit']", timeout=5000)
                return True
            except:
                return False
