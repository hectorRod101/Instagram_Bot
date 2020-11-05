# Created By: Hector Rodriguez
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import os, time, sys, random
from bot import InstagramBot
from os.path import abspath, dirname
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

BASE_PATH = abspath(dirname(__file__))
FILE_PATH = BASE_PATH + '/comment.txt'

def menu():
    """Display main menu for Bot."""
    print('-------------- Instagram Bot --------------')
    print('1) Sign Up')
    print('2) Log In')
    print('3) Exit')
    print('--------------------------------------------')
    val = input('Enter option 1-3: ')
    return val

def menu_selection(val, bf):
    """Select main menu option."""

    # Sign up for new Bot Account or Account.
    if val == 1:
        # Create new bot account.
        botNew = InstagramBot()
        botNew.sign_up()
    # Already have an Account or Bot Account.
    elif val == 2:
        # Create Bot with parameters.
        # ******************************
        # IMPORTANT: Delete parameters USERNAME and PASSWORD and enter YOUR log in information.
        # ******************************
        botOld = InstagramBot('USERNAME', 'PASSWORD')
        driver = botOld.driver

        # Log into Account.
        botOld.log_in()

        # Incase save info pops up on screen.
        botOld.save_info()
        time.sleep(2)
        botOld.save_info()

        # Incase suggested users pops on screen.
        bf.suggested_for_you(driver)
        return botOld
    else:
        # Exit Instagram Bot program.
        bf.exit_bot()

def check_option(val, home):
    """Check whether main menu option is valid."""
    try:
        # Change option to integer.
        val = int(val)

        # Option is not in the range.
        if val <= 0 or val > 3:
            print('Not an option, please try again.\n\n\n')
            return val, home
        home = False
        return val, home
    except ValueError:
        # Option is not an integer.
        print('Please enter an integer 1-3.\n\n\n')
        home = True
        return val, home

def exit_bot():
    """Option to exit Instagram Bot Program."""
    sys.exit("Exiting Instagram Bot Program.\n\n")

def menu_log_in():
    """Display Bot log in options."""
    print("\n\n***** Currently In Bot Home Screen *****")
    print('-------------- Instagram Bot Log In Options --------------')
    print('1) Suggested For You Add Random People')
    print('2) Comment On Post')
    print('3) Like Picture(s)')
    print('4) Search Account')
    print('5) Log Out')
    print('---------------------------------------------------------')
    val = input('Enter option 1-5: ')
    return val

def menu_selection_log_in(val, bf, driver):
    if val == 1:
        # Add suggested for you accounts.
        bf.suggested_for_you(driver)
    elif val == 4:
        bf.search_account(bf, driver)
    
def check_option_log_in(val, home):
    """Check if Instagram Bot log in option is valid."""
    try:
        # Change option to integer.
        val = int(val)

        # Check if option is in range.
        if val <= 0 or val > 5:
            print('Not an option, please try again.\n\n\n')
            return val, home
        home = False
        return val, home
    except ValueError:
        # Option is not an integer.
        home = True
        print('Please enter an integer 1-5.\n\n\n')
        return val, home

def suggested_for_you(driver):
    """Controls suggested for you accounts."""
    # Define how many accounts to add. 
    # Can be changed.
    ACCOUNT_TO_ADD = 2

    print("\n\n***** Currently In Bot Home Screen *****")

    # There are two different "suggested for you" when you create an account. 
    # This decides which page you are currently on.
    if driver.find_elements_by_xpath("//*[contains(text(), 'Suggestions For You')]"):
        # Prompt user if they would like to add accounts.
        print("Would you like to add ["+ str(ACCOUNT_TO_ADD) +"] random accounts?")
        answer = input('Y/N: ')

        # Yes or No to add accounts.
        if answer == 'Y' or answer == 'y':
            while ACCOUNT_TO_ADD > 0:
                # Pause and click Follow.
                time.sleep(4)
                driver.find_element_by_xpath("//button[contains(.,'Follow')]").click()
                time.sleep(4)

                # If webapp finds suspicious activity.
                # Clicks button and try later.
                if driver.find_elements_by_xpath("//button[contains(.,'Report a Problem')]"):
                    driver.find_element_by_xpath("//button[contains(.,'Report a Problem')]").click()
                    print("\n* * * * * * Report a Problem Appeared * * * * * *\n\n")
                    break
                
                # Add account, reduce count, and refresh page.
                ACCOUNT_TO_ADD -= 1
                print("+ Account added.")
                driver.refresh()
        else:
            # No accounts added.
            print("Didn't add any accounts.\n\n")
    else:
        # Go to home page to add accounts.
        # There are two different links to home page.
        if driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img'):
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()
        else:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[1]/a/div/div/img').click()
        
        # Yes or No.
        print("Would you like to add ["+ str(ACCOUNT_TO_ADD) +"] random accounts?")
        answer = input('Y/N: ')

        # Decision.
        if answer == 'Y' or answer == 'y':
            while ACCOUNT_TO_ADD > 0:
                # Pause and click Follow.
                time.sleep(4)
                driver.find_element_by_xpath("//button[contains(.,'Follow')]").click()
                time.sleep(4)

                # If webapp finds suspicious activity.
                # Clicks button and try later.
                if driver.find_elements_by_xpath("//button[contains(.,'Report a Problem')]"):
                    driver.find_element_by_xpath("//button[contains(.,'Report a Problem')]").click()
                    print("\n* * * * * * Report a Problem Appeared * * * * * *\n\n")
                    break

                # Add account, reduce count, and refresh page.
                ACCOUNT_TO_ADD -= 1
                print("+ Account added.")
                driver.refresh()
        else:
            # No accounts added.
            print("Didn't add any accounts.\n\n")

def search_person(bf, driver, search):
    """Search for account to visit, add, or delete."""
    # Decide search.
    if search == 'Y' or search == 'y':
        # Search has two different pages.
        # Decides on current page.
        if driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'):  
            # Ask for username, search, and click.
            print("one")          
            print("\n\nEnter username or name to search.")
            username = input("-----> ")
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(username)  
            time.sleep(3) 
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click() 

            # Get account username.
            time.sleep(2)
            
            if driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1'):
                user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1').text
            else:
                user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text
                
            # Account options.
            search_account_options(bf, driver, user)
        else:
            # Ask for username, search, and click.   
            print("two")       
            print("\nEnter username or name to search.")
            username = input("-----> ")
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[2]/input').send_keys(username)  
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[2]/div[3]/div[2]/div/a[1]').click()

            # Get account username.
            time.sleep(2)
            
            if driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1'):
                user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1').text
            else:
                user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text

            # Account options.
            search_account_options(bf, driver, user)
    # Decide random search.
    else:
        if driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'):
            driver.find_element_by_xpath("//input[@name='username']").send_keys(username)        
        else:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[2]/input')

def search_account(bf, driver):
    """Search by username or random."""
    print("\n\n-------------- Search Account --------------")
    print("Search by username or by random bot search.")
    print("Y: Search By Username/Name")
    print("N: Random Bot Search")
    print("--------------------------------------------")
    search = input("Y/N: ")
    bf.search_person(bf, driver, search)

def search_account_options(bf, driver, user):
    
    home = True

    while home:
        print("\n\n*** Currently on "+ str(user) + "'s account. ***")
        print("\n-------------- Options  --------------")
        print("1) Follow")
        print("2) Unfollow")
        print("3) Comment")
        print("4) Like")
        print("5) Log Out")
        print("----------------------------------------")
        val = input('Enter option 1-5: ')

        val, home = check_search_account_options(val, home)
    
    if val == 5:
        bf.log_out(bf, driver)
    else:
        search_account_options_select(val, bf, driver, user)

def check_search_account_options(val, home):
    """Check if current account option is valid."""
    try:
        # Change option to integer.
        val = int(val)

        # Check if option is in range.
        if val <= 0 or val > 5:
            print('*********************************')
            print('Not an option, please try again.\n')
            return val, home
        home = False
        return val, home
    except ValueError:
        # Option is not an integer.
        home = True
        print('*********************************')
        print('Please enter an integer 1-5.\n\n\n')
        return val, home

def search_account_options_select(val, bf, driver, user):
    if val == 1:
        # Follow selected.
        bf.follow(bf, driver, user)
    elif val == 2:
        # Unfollow selected.
        bf.unfollow(bf, driver, user)
    elif val == 3:
        # Comment selected.
        bf.comment(bf, driver, user)
 

def follow(bf, driver, user):
    """Follow account."""
    if driver.find_elements_by_xpath("//button[contains(.,'Follow')]"):
        driver.find_element_by_xpath("//button[contains(.,'Follow')]").click()
        print("+ Send/Follow Request to "+ str(user))

        time.sleep(2)
        # If webapp finds suspicious activity.
        # Clicks button and try later.
        if driver.find_elements_by_xpath("//button[contains(.,'Report a Problem')]"):
            driver.find_element_by_xpath("//button[contains(.,'Report a Problem')]").click()
            print("\n* * * * * * Report a Problem Appeared * * * * * *\n\n")
        
        # Go to back to home page.
        # There are two different links to home page.
        if driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img'):
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()
        else:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[1]/a/div/div/img').click()
        
    else:
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("You already follow "+ str(user) +".")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

        bf.search_account_options(bf, driver, user)

def unfollow(bf, driver, user):
    """Unfollow account."""
    if driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button'):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
        
        time.sleep(3)
        if driver.find_elements_by_xpath("//button[contains(.,'Unfollow')]"):
            driver.find_element_by_xpath("//button[contains(.,'Unfollow')]").click()
        
        time.sleep(4)
        # If webapp finds suspicious activity.
        # Clicks button and try later.
        if driver.find_elements_by_xpath("//button[contains(.,'Report a Problem')]"):
            driver.find_element_by_xpath("//button[contains(.,'Report a Problem')]").click()
            print("\n* * * * * * Report a Problem Appeared * * * * * *\n\n")
            print("- Unsuccessful unfollow of account "+ str(user))
        else:
            print("- Unfollow "+ str(user) +" success!")
    
        # Go to back to home page.
        # There are two different links to home page.
        if driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img'):
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()
        else:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[1]/a/div/div/img').click()
        
    # Can't unfollow because you don't follow account
    else:
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("You don't follow "+ str(user) +".")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

        bf.search_account_options(bf, driver, user)

def comment(bf, driver, user):
    """Comment on random picture."""
    randInt1 = random.randrange(1, 50)
    randInt2 = random.randrange(1, 3)
    locator = '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[{0}]/div[{1}]'.format(randInt1, randInt2); 
    
    try:
        driver.find_elements_by_xpath(locator)
        driver.find_element_by_xpath(locator).click()
        bf.comment_section(bf, driver, user)
    except NoSuchElementException:
        # Try again.
        comment(bf, driver, user)

def comment_section(bf, driver, user):

    file1 = open(FILE_PATH, "r")
    comments = file1.read()
    content_list = comments.splitlines()
    
    for line in content_list:
        try:
            time.sleep(10)
            driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div').click()
            time.sleep(10)
            driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(line)
            time.sleep(10)
            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()
        except ElementNotInteractableException:
            time.sleep(10)
            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()
    
    file1.close()
    print("Successfully commented on picture.")
    print("Exiting picture.")
    driver.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
    bf.search_account_options(bf, driver, user)


#def like(driver):

def log_out(bf, driver):
    """Log out when signed into account."""
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div[2]').click()
    print("Logging out...........")
    print("Ended Instagram Bot.\n\n\n")
    bf.exit_bot()

