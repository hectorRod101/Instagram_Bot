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

