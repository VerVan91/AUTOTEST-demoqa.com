from selenium.webdriver.common.by import By
from framework.Driver.WebDriver import WebDriver
from framework.Pages.BaseForm import BaseForm
from framework.WebElements.BaseElement import BaseElement
from framework.WebElements.Button import Button
from framework.WebElements.Input import Input
from framework.Utils.Logger import Logger


class WebTablesPage(BaseForm):
    WEB_TABLES_PAGE_LOCATOR = (By.XPATH, "//*[@class = 'main-header' and text() = 'Web Tables']")
    WEB_TABLES_PAGE_NAME = "frames_page"
    WEB_TABLES_BTN_ADD_LOCATOR = (By.ID, "addNewRecordButton")
    WEB_TABLES_BTN_ADD_NAME = "btn_add"
    REG_FORM_LOCATOR = (By.ID, "registration-form-modal")
    REG_FORM_NAME = "registration_form"
    REG_FORM_FIRST_NAME_LOCATOR = (By.ID, "firstName")
    REG_FORM_FIRST_NAME_NAME = "reg_form_first_name"
    REG_FORM_LAST_NAME_LOCATOR = (By.ID, "lastName")
    REG_FORM_LAST_NAME_NAME = "reg_form_last_name"
    REG_FORM_EMAIL_LOCATOR = (By.ID, "userEmail")
    REG_FORM_EMAIL_NAME = "reg_form_email"
    REG_FORM_AGE_LOCATOR = (By.ID, "age")
    REG_FORM_AGE_NAME = "reg_form_age"
    REG_FORM_SALARY_LOCATOR = (By.ID, "salary")
    REG_FORM_SALARY_NAME = "reg_form_salary"
    REG_FORM_DEPARTMENT_LOCATOR = (By.ID, "department")
    REG_FORM_DEPARTMENT_NAME = "reg_form_department"
    BTN_SUBMIT_LOCATOR = (By.ID, "submit")
    BTN_SUBMIT_NAME = "btn_submit"
    ADDED_USERS_LOCATOR = (By.XPATH, "//*[contains(@class, 'rt-tr ')] [not(contains(@class, '-padRow'))]")
    ADDED_USERS_NAME = "added_users"

    def __init__(self):
        super().__init__(self.WEB_TABLES_PAGE_LOCATOR, self.WEB_TABLES_PAGE_NAME)
        self.btn_add = Button(self.WEB_TABLES_BTN_ADD_LOCATOR, self.WEB_TABLES_BTN_ADD_NAME)
        self.reg_form_first_name = Input(self.REG_FORM_FIRST_NAME_LOCATOR, self.REG_FORM_FIRST_NAME_NAME)
        self.reg_form_last_name = Input(self.REG_FORM_LAST_NAME_LOCATOR, self.REG_FORM_LAST_NAME_NAME)
        self.reg_form_email = Input(self.REG_FORM_EMAIL_LOCATOR, self.REG_FORM_EMAIL_NAME)
        self.reg_form_age = Input(self.REG_FORM_AGE_LOCATOR, self.REG_FORM_AGE_NAME)
        self.reg_form_salary = Input(self.REG_FORM_SALARY_LOCATOR, self.REG_FORM_SALARY_NAME)
        self.reg_form_department = Input(self.REG_FORM_DEPARTMENT_LOCATOR, self.REG_FORM_DEPARTMENT_NAME)
        self.btn_submit = Button(self.BTN_SUBMIT_LOCATOR, self.BTN_SUBMIT_NAME)
        self.reg_form = BaseElement(self.REG_FORM_LOCATOR, self.REG_FORM_NAME)
        self.added_users = BaseElement(self.ADDED_USERS_LOCATOR, self.ADDED_USERS_NAME)

    def click_btn_add(self):
        self.btn_add.click()

    def type_first_name(self, text):
        self.reg_form_first_name.send_keys(text)

    def type_last_name(self, text):
        self.reg_form_last_name.send_keys(text)

    def type_email(self, text):
        self.reg_form_email.send_keys(text)

    def type_age(self, text):
        self.reg_form_age.send_keys(text)

    def type_salary(self, text):
        self.reg_form_salary.send_keys(text)

    def type_department(self, text):
        self.reg_form_department.send_keys(text)

    def click_btn_submit(self):
        self.btn_submit.click()

    def is_reg_form(self):
        try:
            if len(self.reg_form.get_elements()) == 0:
                return False
            return self.reg_form.get_elements()
        except Exception as e:
            Logger.log_warning(f"{self.name} exception '{e}' from func is_alert ")
            return False

    def count_added_users(self):
        elements = self.added_users.get_elements()
        return len(elements)

    @staticmethod
    def searching_user_data(arr):
        res = []
        for param in arr:
            res.append(WebDriver.get_driver().find_element(By.XPATH, f"//*[text() = '{param}']").text)
        return set(res)

    @staticmethod
    def delete_user(number):
        WebDriver.get_driver().find_element(By.ID, f"delete-record-{number}").click()
