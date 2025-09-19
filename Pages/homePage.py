import allure
import allure
from playwright.sync_api import Page
from conftest import page

class HomePage:
    
    def __init__(self, page: Page):
        self.page = page
        
    def open_profile_dropdown(self):
        self.page.click(".oxd-userdropdown-icon")
    
    @allure.step("Checking profile dropdown menu")    
    def is_everything_in_dropdown(self):
        self.open_profile_dropdown()
        self.page.wait_for_selector("text=About", timeout=5000)
        self.page.wait_for_selector("text=Support")
        self.page.wait_for_selector("text=Change password")
        self.page.wait_for_selector("text=Logout")
        
    @allure.step("Checking if a user has been logged in")        
    def is_logged_in(self)-> bool:  
            try:
                self.open_profile_dropdown()
                self.page.wait_for_selector("text=Logout", timeout=5000)
                return True
            except:
                return False
            
    @allure.step("Logout")
    def logout(self):
            self.is_logged_in()
            self.page.click("text=Logout")
            
    
