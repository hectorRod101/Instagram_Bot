# Created By: Hector Rodriguez
from selenium.webdriver.common.by import By
from selenium import webdriver
import os, time, sys
import bot_functions as bf


class InstagramBot:
    def __init__(self, username = None, password = None):
        """Initialize parameters for Instagram login."""
        self.username = username
        self.password = password
        
        self.driver = webdriver.Chrome(executable_path='/Users/hectorrodriguez/Desktop/instaBot/chromedriver')
    
    def sign_up(self):
        """Bot for signing up for Instagram."""
        self.driver.get('https://www.instagram.com/accounts/emailsignup/')

    def log_in(self):
        """Bot to log onto instagram with valid credits."""
        print("Logging in.........")
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1) # pause
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        time.sleep(1) # pause
        self.driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
        time.sleep(5) # pause
        print("Successfully logged in.\n")

    def save_info(self):
        """When save info appears onto screen."""
        print("Save info screen.")
        if self.driver.find_element_by_xpath("//button[contains(.,'Not Now')]"):
            self.driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()

if __name__ == '__main__':
    home = True
    # Set loop for menu.
    while home:
        # Check main menu bot options.
        val = bf.menu()

        # Check if it's a valid option.
        val, home = bf.check_option(val, home)

        # If valid option, run option.
        if not home:
            bot = bf.menu_selection(val, bf)

    home_log_in = True
    # Set loop for log in menu.
    while home_log_in:
        # Check login in menu bot options.
        val2 = bf.menu_log_in()

        # Check if it's a valid option.
        val2, home_log_in = bf.check_option_log_in(val2, home_log_in)

        # If valid option, run option.
        if not home_log_in and val2 != 5:
            home_log_in = True
            bf.menu_selection_log_in(val2, bf, bot.driver)
        elif val2 == 5:
            # Option log out.
            bf.log_out(bf, bot.driver)
