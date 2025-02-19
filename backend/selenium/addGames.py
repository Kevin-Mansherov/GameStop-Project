# /opt/anaconda3/bin/python sel.py
# Import statements
from selenium import webdriver  # Main Se


# selenium package for browser automation
# Manages ChromeDriver service
from selenium.webdriver.chrome.service import Service

# Chrome-specific configuration options
from selenium.webdriver.chrome.options import Options

# Provides locator strategies (ID, CLASS, etc.)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Implements explicit waits

# Conditions for WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # For adding delays between actions

# Function to set up the Chrome WebDriver
import pandas as pd
import re
import requests

def setup_driver():
    chrome_options = Options()  # Create a new Options object for Chrome
    service = Service()  # Create a new Service object to manage ChromeDriver
    # Initialize Chrome with our settings
    return webdriver.Chrome(service=service, options=chrome_options)


def handle_alert(driver):
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert  
        print(f"Alert found: {alert.text}") 
        alert.accept() 
        time.sleep(1)  
    except:
        print("No alert found") 

def GetGamesFromStream():
    driver = setup_driver()
    try:
        sheetsURL = "https://docs.google.com/spreadsheets/d/1iv1SNMtKWdvu9vYxucryxMo_RC7rSph4h4_fheBe-Is/export?format=csv"
        driver.get("https://store.steampowered.com/")
        
        time.sleep(10)

        games = driver.find_elements(By.CSS_SELECTOR, "a.tab_item")
        games_list = []

        for game in games[:5]:
            title = game.find_element(By.CSS_SELECTOR,".tab_item_name").text
            creator = "steam"
            year = game.find_element(By.CSS_SELECTOR,".release_date").text
            type = game.find_element(By.CSS_SELECTOR,".tab_item_top_tags").text
            price = game.find_element(By.CSS_SELECTOR,".discount_final_price").text
            available = 1
            price = re.sub(r"[^\d.]", "", price)

            games_list.append([title,creator,year,type,price,available])

        data_frame = pd.DataFrame(games_list,columns=["title","creator","year","type","price","available"])

        csv_data = data_frame.to_csv(index=False)
        response = requests.put(sheetsURL,data=csv_data,headers={"Content-Type": "text/csv"})
        if response.status_code == 200:
            print("Successfully updated google sheets.\n")
        else:
            print(f"Failed to update: {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

def AddGamesToWeb():
    driver = setup_driver()  # Create a new browser instance

    try:
        url = "https://docs.google.com/spreadsheets/d/1iv1SNMtKWdvu9vYxucryxMo_RC7rSph4h4_fheBe-Is/export?format=csv"
        info = pd.read_csv(url)

        # Open the website
        # Navigate to the specified URL
        driver.get("http://127.0.0.1:5500/frontend/index.html")
        # Create a wait object with 10-second timeout
        wait = WebDriverWait(driver, 10)

        # Handle the name field
        login_field = wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )  # Wait until name field is present
        login_field.send_keys("kevin@gmail.com")  # Type "John"
        time.sleep(1)  # Wait 1 second
        login_field = wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        login_field.send_keys("123")  # Add "Doe"
        time.sleep(1)  # Wait again

        # Handle form submission
        login_button = driver.find_element(By.ID, "login")  # Find submit button
        login_button.click()  # Click the submit button

        handle_alert(driver)
        time.sleep(3)

        for index,row in info.iterrows():
            title = row["title"]
            creator = row["creator"]
            year = row["year_published"]
            game_type = row["type"]
            price = row["price"]
            available = row["available"]

            driver.find_element(By.ID, "game-title").send_keys(title)
            time.sleep(1) 
            driver.find_element(By.ID, "game-creator").send_keys(creator)
            time.sleep(1) 
            driver.find_element(By.ID, "game-year-published").send_keys(year)
            time.sleep(1) 
            driver.find_element(By.ID, "game-type").send_keys(game_type)
            time.sleep(1) 
            driver.find_element(By.ID, "game-price").send_keys(price)
            time.sleep(1) 
            driver.find_element(By.ID, "amount-to-add").send_keys(available)
            time.sleep(1) 

            addGame_button = driver.find_element(By.ID,"addGameID")
            addGame_button.click()

            handle_alert(driver)

            wait = WebDriverWait(driver, 4)
        

        # Wait for user input before closing
        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Script entry point
# Only run if this file is run directly (not imported)
if __name__ == "__main__":
    GetGamesFromStream()
    # AddGamesToWeb()  # Start the form interaction process