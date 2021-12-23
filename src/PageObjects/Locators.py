# http://demo.testarena.pl/zaloguj
# "*" to przejaw mojego lenistwa
class Locators(object):

    login_button = "//*[@id='login']"
    login_email_adress_field= "//*[@id='email']"
    login_password_field = "//*[@id='password']"

# http://demo.testarena.pl/rh/tasks
    expectedTask = "//*[@name='item_6642']"
    #     add_task_button = "//*[@href='http://demo.testarena.pl/rh/task_add']"
    # http://demo.testarena.pl/rh/task_add
    # 3 znaki
    title = "//*[@id='title']"
    description = "//*[@id='description']"
    # 3 znaki env1
    environment = "//*[@id='token-input-environments']"
    # 2 znaki 1A
    version = "//*[@id='token-input-versions']"
    # format 2021-12-31 23:59
    date = "//*[@id='dueDate']"
    assign_text = "//*[@id='j_assignToMe']"
    save_button = "//*[@id='save']"


#  modal //body/div/p Task successfully added!
# url ma task id do wykorzystania [^/]*$




