"""
This file is the main meat of the pie. Running selenium to open and run through web pages.
Goals are to enter text into a page. Assert conent to make sure it's correct. Loop through items.
"""
    
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WEBDRIVER_PATH = "C:\Testing\chromedriver.exe"
driver = webdriver.Chrome(WEBDRIVER_PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
    
except:
    driver.quit()



time.sleep(5)

driver.quit()