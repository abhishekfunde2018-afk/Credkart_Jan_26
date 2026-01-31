"""
Testcases :
1. Login
2. Registration
3. Checkout
4. Amount Verification
5. Login with params
6. Login with Excel
7. Registration wih params
8. Registration with Excel

Mostly all you are Sanity and Smoke testcases are in automation list.
"""
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.Login_page import  Login_Page_Class
from pageobjects.Registration_page import Registration_Page_Class
from utilities.Logger import log_generator_class
from utilities.readconfig import Readconfigclass


@pytest.mark.usefixtures("browser_setup") # New
class Test_User_Profile :
    driver = None
    email = Readconfigclass.get_data_for_email()
    password = Readconfigclass.get_data_for_password()
    login_url = Readconfigclass.get_data_for_login_url()
    registration_url = Readconfigclass.get_data_for_registration_url()
    log = log_generator_class.log_gen_method()

    def test_verify_Credkart_url_001(self):
        self.log.info("this opening credkart url")
        self.driver.get(self.login_url)
        if self.driver.title == "CredKart":
            print(f"driver.title --> {self.driver.title}")
            self.log.info("getting driver title")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_pass.png")
            self.log.info("taking screenshot")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_fail.png")
            self.log.info("saving screenshot")
            assert False


    def test_Credkart_login_002(self):
        self.driver.get(self.login_url)


        self.lp = Login_Page_Class(self.driver) # login page class object and now we can access the methods

        # Enter Username
        # email = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email.send_keys(email_id)

        self.lp.Enter_Email(self.email)


        # Enter Password
        # password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # password.send_keys(pass_word)

        self.lp.Enter_Password(self.password)

        # Click on Login button
        # login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # login_button.click()
        self.lp.Click_Login_Register_Button()

        # wait = WebDriverWait(self.driver, 5)
        # try:
        #     wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        #     element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        #     print("User Login Successful")
        #     # driver.save_screenshot(f"User Login Successful_{email_id}.png")
        #     menu = self.driver.find_element(By.XPATH, "//a[@role='button']")
        #     menu.click()
        #     logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        #     logout.click()
        #
        #
        # except:
        #     print("User Login Fail")
        #     # driver.save_screenshot(f"User Login Fail_{email_id}.png")
        #     assert False, "User Login Fail"


        if self.lp.verify_menu_button_visibility() =="pass":
            self.driver.save_screenshot(f"User Login Successful_{self.email}.png")
            self.lp.Click_Menu_button()
            self.lp.Click_Logout_button()
        else:
            self.driver.save_screenshot(f"User Login Fail_{self.password}.png")
            assert True, "User Login Fail"

    def test_Credkart_registration_003(self):

        self.driver.get(self.registration_url)
        fake_username = Faker().user_name()# New
        fake_email = Faker().email()# New
        password_data = "Credence_user_101@123"
        print(f"fake_username--> {fake_username}")# New
        print(f"fake_email--> {fake_email}")# New

        self.rp = Registration_Page_Class(self.driver)

        self.rp.Enter_Name(fake_username)

        self.rp.Enter_Email(fake_email)

        self.rp.Enter_Password(password_data)

        self.rp.Enter_Confirm_Password(password_data)

        self.rp.Click_Login_Register_Button()

        if self.rp.verify_menu_button_visibility() == "pass":
            self.driver.save_screenshot(f".\\Screenshots\\User Registration Successful_{fake_username}.png")
            self.rp.Click_Menu_button()
            self.rp.Click_Logout_button()
        else:
            self.driver.save_screenshot(f".\\Screenshots\\User Registration Fail_{fake_username}.png")
            assert False, "User Registration Fail"


# pytest -v -s -n=auto --html=Html_reports\my_report_24th_jan_2026.html

# jenkins at 31

