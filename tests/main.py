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
    
    # def test_title(self):
    #     main_page = page.MainPage()
    #     assert main_page.is_title_matches()
        
    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    
if __name__ == "__main__":
     unittest.main()