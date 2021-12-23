import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.TestBase.Setup import Setup
from src.PageObjects.Pages.LoginPage import LoginPage
from src.PageObjects.Pages.AddTaskPage import AddTask
import unittest
import re


class test_NewTask(Setup):
    login = "administrator@testarena.pl"
    password = "sumXQQ72$L"
    login_url = "http://demo.testarena.pl/zaloguj"

    expectedProject = "rh"
    # precondition projekt musi istniec i miec odpowiednie uprawnienia

    ulr_to_tasks = "http://demo.testarena.pl/" + expectedProject + "/tasks"
    url_to_add_task_page = "http://demo.testarena.pl/" + expectedProject + "/task_add"

    # na potrzeby zadania wbite na sztynow przy normalnych testach jakis precondition na istnienie env/version
    title = "ABC"
    description = "Some text"
    # kolejne dwa przykady koniecznych warunkw
    environment = "env1"
    version = "1A"
    ###
    date = "2021-12-31 23:59"

    def test_Add_New_Task(self):
        driver = self.driver

        self.loginToArena()
        self.fillNewTaskForm()

        url_to_task_id = driver.current_url
        task_id = re.search('[^/]*$', url_to_task_id)
        task_id = task_id.group(0)
        driver.get(self.ulr_to_tasks)

        expectedTask = "//*[@name='item_" + task_id + "']"
        isTaskCreated = driver.find_element(By.XPATH, expectedTask)
        # w zasadzie ta czesc tutaj jest niepotrzebna test przewrci sie w momencie kiedy nie znajdzie webelementu ale caosc mona adnie opakowac dalej
        assert bool(isTaskCreated)

    def loginToArena(self):
        driver = self.driver
        driver.get(self.login_url)
        driver.set_page_load_timeout(30)
        loginPage = LoginPage(driver)

        loginPage.email.send_keys(self.login)
        loginPage.password.send_keys(self.password)
        loginPage.zaloguj_button.click()

    def fillNewTaskForm(self):
        driver = self.driver
        driver.get(self.url_to_add_task_page)
        newTask = AddTask(driver)

        newTask.title.send_keys(self.title)
        newTask.description.send_keys(self.description)
        newTask.environment.send_keys(self.environment)
        sleep(1)
        newTask.environment.send_keys(Keys.ENTER)

        newTask.version.send_keys(self.version)
        sleep(1)
        newTask.version.send_keys(Keys.ENTER)

        newTask.date.send_keys(self.date)
        newTask.assign_text.click()
        newTask.save_button.click()
        sleep(1)

    if __name__ == '__main__':
        unittest.main()
