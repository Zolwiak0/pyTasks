from selenium.webdriver.common.by import By
from src.PageObjects.Locators import Locators


class AddTask(object):
    #w konstruktorze lista elementw na stronie do interakci
    def __init__(self, driver):
        self.driver = driver
        self.title = driver.find_element(By.XPATH, Locators.title)
        self.description = driver.find_element(By.XPATH, Locators.description)
        self.environment = driver.find_element(By.XPATH, Locators.environment)
        self.version = driver.find_element(By.XPATH, Locators.version)
        self.date = driver.find_element(By.XPATH, Locators.date)
        self.assign_text = driver.find_element(By.XPATH, Locators.assign_text)
        self.save_button = driver.find_element(By.XPATH, Locators.save_button)



