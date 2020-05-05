import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PythonProject.base import Page
from PythonProject.locators import *
from selenium.webdriver.support.ui import WebDriverWait


# Page objects are written in this module.

class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text

    def click_sign_up_button(self):
        self.hover(*self.locator.ACCOUNT)
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpPage(self.driver)

    def click_sign_in_button(self):
        self.hover(*self.locator.ACCOUNT)
        self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)


    def login_with_valid_user(self):
        self.find_element(*self.locator.EMAIL).send_keys("userid")
        self.find_element(*self.locator.EMAIL).send_keys(Keys.RETURN)
        self.find_element(*self.locator.PASSWORD).send_keys("password")
        self.find_element(*self.locator.SUBMIT).click()
        return HomePage(self.driver)

    def login_with_in_valid_user(self):
        self.find_element(*self.locator.EMAIL).send_keys("userid@gmoil.com")
        self.find_element(*self.locator.EMAIL).send_keys(Keys.RETURN)
        return self.find_element(*self.locator.ERROR_MESSAGE).text


class HomePage(Page):
    pass


class SignUpPage(Page):
    pass
