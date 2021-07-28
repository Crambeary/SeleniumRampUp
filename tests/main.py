import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:\Testing\chromedriver.exe")
        self.driver.get("http://www.python.org")
        return super().setUp()
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()
    
    
if __name__ == "__main__":
     unittest.main()