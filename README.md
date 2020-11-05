# Instagram_Bot
[![Language](https://img.shields.io/badge/language-python-blue.svg?style=flat)](https://www.python.org)</br>
Simple Instagram Bot to interact with [Instagram](https://www.instagram.com) to perform automated tasks
faster than a human.

## Prerequisites

- If you don't have [Python](https://www.python.org/downloads/) installed.
- If you don't have [Selenium](https://pypi.org/project/selenium/) installed.</br></br>
Depending on Browser:
- If you don't have [ChromeDrive](https://chromedriver.chromium.org) installed.
- Look into [ChromeDrive](https://chromedriver.chromium.org/getting-started) documentation how to setup.</br>
-> Make sure to move Drive into main project folder.

## Usage
### Step 1: Change this part of the code.
```bash
 # Create Bot with parameters.
        # ******************************
        # IMPORTANT: Delete parameters USERNAME and PASSWORD and enter YOUR log in information.
        # ******************************
        botOld = InstagramBot('USERNAME', 'PASSWORD')
        driver = botOld.driver
```
### Step 2: Prerequisites completed.
```bash
cd Instagram_Bot
python3 bot.y
```
### Step 3: Main menu.
* * * Option 1 not implemented. Only 2 and 3 are functional. * * *</br>

<img src="https://i.imgur.com/BrVI2JX.png" width="700" height="200" />

Can change how many accounts can be followed.
```bash
 # Define how many accounts to add. 
    # Can be changed.
    ACCOUNT_TO_ADD = 2
```
<img src="https://i.imgur.com/QedCUmL.png" width="700" height="200" />

### Step 4: Bot menu.
* * * Option 2 and 3 not implemented. Only 1, 4, and 5 are functional. * * *</br>

<img src="https://i.imgur.com/8pZj1aq.png" width="700" height="200" />
- Option 1: Follows accounts that are suggested to you.</br>
- Option 2: You are able to search for a specific account.</br>
- Option 3: Log out of instagram bot.</br>

### Search Account Menu
* * * Option N not implemented. Only Y functional. * * *</br>

<img src="https://i.imgur.com/SDHQvHa.png" width="700" height="200" />
- Option Y: Searches account by given user.</br>
- Option N: Not implemented.</br>

Will select the first account that appears.</br>
<img src="https://i.imgur.com/BHuWK4B.png" width="700" height="200" />

