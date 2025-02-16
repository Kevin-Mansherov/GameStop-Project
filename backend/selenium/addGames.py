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

def setup_driver():
    chrome_options = Options()  # Create a new Options object for Chrome
    service = Service()  # Create a new Service object to manage ChromeDriver
    # Initialize Chrome with our settings
    return webdriver.Chrome(service=service, options=chrome_options)


def interact_with_form():
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

        time.sleep(3)

        for index,row in info.iterrows():
            title = row["title"]
            creator = row["creator"]
            year = row["year_published"]
            game_type = row["type"]
            price = row["price"]
            available = row["available"]

        

        

        # Wait for user input before closing
        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Script entry point
# Only run if this file is run directly (not imported)
if __name__ == "__main__":
    interact_with_form()  # Start the form interaction process