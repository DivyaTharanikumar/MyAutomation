import unittest
from selenium import webdriver
from PythonProject.pages import *
from PythonProject.testCases import test_cases
from PythonProject.locators import *
from selenium.webdriver.common.by import By

class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\srifo\\chromedriver_win32\\chromedriver.exe')
        self.driver.get("http://www.amazon.com")

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        search_result = page.search_item("Nexus 5")
        self.assertIn("Nexus 5", search_result)

    def test_sign_up_button(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        signUpPage = page.click_sign_up_button()
        self.assertIn("ap/register", signUpPage.get_url())

    def test_sign_in_button(self):
        print ("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        loginPage = page.click_sign_in_button()
        self.assertIn("ap/signin", loginPage.get_url())

    def test_sign_in_with_valid_user(self):
        print ("\n" + str(test_cases(4)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_valid_user()
        self.assertIn("signin&", result.get_url())

    def test_sign_in_with_in_valid_user(self):
        print ("\n" + str(test_cases(5)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user()
        self.assertIn("There was a problem", result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)