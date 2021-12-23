# . Zalogować się do wersji demo
# II. Do dowolnego projektu dodać nowe zadanie i potwierdzić, że zostało dodane.
# III. Przeprowadzić test logowania przy użyciu błędnych danych.
# http://demo.testarena.pl/zaloguj


from src.TestBase.Setup import Setup
from src.PageObjects.Pages.LoginPage import LoginPage
import unittest


class test_LoginPage(Setup):
    login = "administrator@testarena.pl"
    password = "sumXQQ72$L"


    def test_login_with_right_credentials(self):

        driver = self.driver
        self.driver.get("http://demo.testarena.pl/zaloguj")
        self.driver.set_page_load_timeout(30)
        loginPage = LoginPage(driver)


        loginPage.email.send_keys(self.login)
        loginPage.password.send_keys(self.password)
        loginPage.zaloguj_button.click()
        currentTitle = driver.title
        expectedTitle = "Cockpit - TestArena"
        assert expectedTitle == currentTitle
    # na dobra sprawe assercja jest tutaj zbedna, przy niewlasciwych danych mozna sprawedzic czy sa prawidlowe komunikaty

    def test_login_with_wrong_password(self):
        driver = self.driver
        self.driver.get("http://demo.testarena.pl/zaloguj")
        self.driver.set_page_load_timeout(30)
        loginPage = LoginPage(driver)

        loginPage.email.send_keys(self.login)
        loginPage.password.send_keys("Incorrect password")
        loginPage.zaloguj_button.click()
        currentTitle = driver.title
        expectedTitle = "Cockpit - TestArena"
        assert expectedTitle != currentTitle

    def test_login_wrong_email_and_correct_password(self):
        driver = self.driver
        self.driver.get("http://demo.testarena.pl/zaloguj")
        self.driver.set_page_load_timeout(30)
        loginPage = LoginPage(driver)

        loginPage.email.send_keys("Incorrect login")
        loginPage.password.send_keys(self.password)
        loginPage.zaloguj_button.click()
        currentTitle = driver.title
        expectedTitle = "Cockpit - TestArena"
        assert expectedTitle != currentTitle


    if __name__ == '__main__':
        unittest.main()