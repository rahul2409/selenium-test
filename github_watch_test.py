import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GithubWatchRepoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://github.com"
    def test_github_watch_repo_annonymous_user_redirects_to_login(self):
        login_url = "https://github.com/login?return_to=%2FSeleniumHQ%2Fselenium"
        driver = self.driver
        driver.get("{0}/SeleniumHQ/selenium".format(self.base_url))
	watch_button=driver.find_element_by_partial_link_text(u"Watch").click()
	driver.save_screenshot( 'test_github_watch_repo_annonymous_user_redirects_to_login.png' )
    def tearDown(self):
        self.driver.close()

