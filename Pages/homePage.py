import allure
import allure
from playwright.sync_api import Page
from conftest import page

class HomePage:
    
    def __init__(self, page: Page):
        self.page = page
        
    
    @allure.step("Checking if a user has been logged in")        
    def is_logged_in(self):  
        with allure.step("Checking if user is on the homepage"):
            try:
                self.page.click(".oxd-userdropdown-icon")
                self.page.wait_for_selector("text=Logout", timeout=5000)
                return True
            except:
                return False
            
    @allure.step("Logout")
    def logout(self):
        with allure.step("Logout process"):
            self.is_logged_in()
            self.page.click("text=Logout")