"""
This file is the main meat of the pie. Running selenium to open and run through web pages.
Goals are to enter text into a page. Assert conent to make sure it's correct. Loop through items.
"""
    
    
from selenium import webdriver

WEBDRIVER_PATH = "C:\Testing\chromedriver.exe"
driver = webdriver.Chrome(WEBDRIVER_PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()