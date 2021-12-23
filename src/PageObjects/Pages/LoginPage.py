from selenium.webdriver.common.by import By
from src.PageObjects.Locators import Locators


class LoginPage(object):
    #w konstruktorze lista elementw na stronie do interakci
    def __init__(self, driver):
        self.driver = driver
        self.email = driver.find_element(By.XPATH, Locators.login_email_adress_field)
        self.password = driver.find_element(By.XPATH, Locators.login_password_field)
        self.zaloguj_button = driver.find_element(By.XPATH, Locators.login_button)


    def getEmail(self):
            return self.email
    def getPassword(self):
            return self.password
    def getZalogujButton(self):
            return self.zaloguj_button





