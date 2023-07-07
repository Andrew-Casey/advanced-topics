from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time as t
import os


def Get_sql_files():

    # Get user and password from os
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubpass")
                 
    base_url = "https://github.com/"


    # Create a webdriver object 
    driver = webdriver.Chrome(service = Service())

    # Open github
    driver.get(base_url+"login")

    # Navigate to database-exercises repo
    driver.get(base_url+user+"/database-exercises")

    # Identify links to links within repository
    files = driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']")

    # Iterate over the files starting from index 1 (skipping the first readme file)
    for file_index in range(1, len(files)):
    # Re-locate the files after navigating back to the section page
        files = driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']")
        
        file_to_download = files[file_index]
        file_to_download.click()
    
    # Wait for the download button to appear (add appropriate wait time if necessary)
        t.sleep(5)
    
    # Get the download button
        download_button = driver.find_elements(By.XPATH, "//button[@data-component='IconButton']")[5]
        download_button.click()
    
    # Wait for the download to complete (add appropriate wait time if necessary)
        t.sleep(5) 
    
    # Go back to the section page to select the next file
        driver.back()
    
    # Wait for the section page to load (add appropriate wait time if necessary)
        t.sleep(5)

    # Quit and close
    driver.quit()


# Call function
Get_sql_files()