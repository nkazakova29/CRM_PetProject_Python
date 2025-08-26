import allure
from playwright.sync_api import Page

from conftest import page

class LoginPage:
    URL = "https://suitecrm.com/demo/"
    
    def __init__(self, page: Page):
        self.page = page
        
    @allure.step("Open CRM website")
    def open(self):
        self.page.goto(self.URL)
        
    @allure.step("Go to Login Page")    
    def open_login_page(self):
        goto_loginpage = self.page.locator("text=ACCESS THE SUITECRM 7 ESR DEMO")
        goto_loginpage.click()
        
    @allure.step("Sign in process")
    def login(self, username: str, password: str):
        self.page.fill('#user_name', username)
        self.page.fill('#username_password', password)
        self.page.click('#bigbutton')
        
    @allure.step("Checking time zone popup")    
    def time_zone_chosing(self):
        if self.page.is_visible("input#Save"):
            self.page.click("input#Save")
            
    @allure.step("Checking if a user has been logged in")        
    def is_logged_in(self):  
            # Ждем появления заголовка домашней страницы
        try:
            self.page.wait_for_selector("h1:has-text('Welcome to the SuiteCRM 7 Demo')", timeout=5000)
            return True
        except:
            return False
        
        
    @allure.step("Checking if an login error has appeared")    
    def is_error_appeared(self):
        try:
            self.page.wait_for_selector("text=You must specify a valid username and password.", timeout=5000)
            return True
        except:
            return False
    
    