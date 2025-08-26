import allure
from playwright.sync_api import Page

from conftest import page

class LoginPage:
    URL = "https://suitecrm.com/demo/"
    
    def __init__(self, page: Page):
        self.page = page
        

    def open(self):
        with allure.step("Open CRM site"):
            self.page.goto(self.URL)
        
    def open_login_page(self):
        with allure.step("Go to login page"):
            goto_loginpage = self.page.locator("text=ACCESS THE SUITECRM 7 ESR DEMO")
            goto_loginpage.click()

    def login(self, username: str, password: str):
        with allure.step("Sign in process"):
            self.page.fill('#user_name', username)
            self.page.fill('#username_password', password)
            self.page.click('#bigbutton')
        
    def time_zone_chosing(self):
        with allure.step("ОChecking if time zone window has appeared"):
            if self.page.is_visible("input#Save"):
                self.page.click("input#Save")
            
    def is_logged_in(self):  
        with allure.step("Checking if the user is logged in"):
        
    # Ждем появления заголовка домашней страницы
            try:
                self.page.wait_for_selector("h1:has-text('Welcome to the SuiteCRM 7 Demo')", timeout=5000)
                return True
            except:
                return False
        
        
    def is_error_appeared(self):
        with allure.step("Checking if an authorization error has appeared"):
            try:
                self.page.wait_for_selector("text=You must specify a valid username and password.", timeout=5000)
                return True
            except:
                return False
    
    
