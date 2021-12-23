import unittest
from selenium import webdriver
import urllib3


class Setup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            self.driver.close()

            self.driver.quit()

