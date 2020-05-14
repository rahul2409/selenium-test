import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GithubSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://github.com"

    def test_github_repo_search_without_criteria(self):
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.click()
        search_box.send_keys(Keys.RETURN)
        driver.save_screenshot('test_github_repo_search_without_criteria.png')

    def test_github_repo_search_for_selenium(self):
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.click()
        search_box.send_keys("laravel")
        search_box.send_keys(Keys.RETURN)
        driver.save_screenshot('test_github_repo_search_for_selenium.png')

    def test_github_repo_search_with_invalid_string(self):
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.click()
        search_box.send_keys("?*#^*^%")
        search_box.send_keys(Keys.RETURN)
        driver.save_screenshot( 'test_github_repo_search_with_invalid_string.png' )
  
    def tearDown(self):
        self.driver.close()


