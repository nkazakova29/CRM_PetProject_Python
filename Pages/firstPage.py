from playwright.sync_api import Page

from conftest import page

class LoginPage:
    URL = "https://suitecrm.com/demo/"
    
    def __init__(self, page: Page):
        self.page = page
        

    def open(self):
        self.page.goto(self.URL)
        
    def open_login_page(self):
        goto_loginpage = self.page.locator("text=ACCESS THE SUITECRM 7 ESR DEMO")
        goto_loginpage.click()

    def login(self, username: str, password: str):
        self.page.fill('#user_name', username)
        self.page.fill('#username_password', password)
        self.page.click('#bigbutton')
        
    def time_zone_chosing(self):
        if self.page.is_visible("input#Save"):
            self.page.click("input#Save")
            
    def is_logged_in(self):
    # Ждем появления заголовка домашней страницы
        try:
            self.page.wait_for_selector("h1:has-text('Welcome to the SuiteCRM 7 Demo')", timeout=5000)
            return True
        except:
            return False
    
    