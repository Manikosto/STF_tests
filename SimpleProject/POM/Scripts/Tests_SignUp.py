__author__ = 'Alexey Koledachkin'
import datetime
import allure
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POM.Pages.ContactUs import ContactUs
from POM.TestBase.EnvironmentSetUp import EnvironmentSetup
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from POM.locators import Locator
from POM.TestBase.Functions import Functions
from POM.Pages.SignUp import SignUp
from POM.Pages.Yandex import YandexLogin
from POM.TestBase.Links import Links
from POM.Pages.LoginPage import Login
from POM.Data import Data

class SignUpPage(EnvironmentSetup):

###   INIT   ###


    def INIT(self, page=Links.sign_up):
        driver = self.driver
        self.driver.get(page)
        self.function = Functions(driver)
        self.signup = SignUp(driver)
        self.yandex = YandexLogin(driver)
        self.locator = Locator()



##   Tests   ###

    # Requaired fields
    @allure.suite("Registration")
    @allure.title("Required fields")
    @allure.description("Open SignUp page and check required fields")
    @allure.severity("Minor")
    def test_RequiredFields(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Title cheking
        with allure.step("Title cheking"):
            self.function.TitleCheck("Registration Page - SimpleTollFree")
        # Required fields checking
        with allure.step("Required fields checking"):
            self.signup.submit.click()
        # Find labels of required field
        with allure.step("Find labels of required field"):
            self.function.WaitLocate(self.locator.r_field)
        #
        with allure.step("Take screenshot"):
            self.function.getScreenshot("rf.PNG")

    # Requaired fields
    @allure.title("Successful registration")
    @allure.suite("Registration")
    @allure.description("Open SignUp page and registration")
    @allure.severity("Blocker")
    def test_CorrectSignUp(self):

        with allure.step("Open page in the browser"):
            self.INIT()

        with allure.step("Title cheking"):
            self.function.TitleCheck("Registration Page - SimpleTollFree")

        with allure.step("Enter Customer Information"):
            self.signup.first_name.send_keys(Data.reg_first_name)
            self.signup.last_name.send_keys(Data.reg_last_name)
            self.signup.email.send_keys(Data.test_login)
            self.signup.phone_num.send_keys(Data.reg_phone_num)
            self.signup.company_name.send_keys(Data.reg_company_name)
            with allure.step("Take Screenshot Customer Information"):
                self.function.getScreenshot("CustomerInfo")

        with allure.step("Enter Customer Address"):
            self.signup.street_address.send_keys(Data.reg_street_address)
            self.signup.suite.send_keys(Data.reg_suite)
            self.signup.city.send_keys(Data.reg_city)
            self.signup.drp_state.select_by_index(4)
            self.signup.zip.send_keys(Data.reg_zip)
            with allure.step("Take Screenshot Customer Address"):
                self.function.getScreenshot("CustomerAddress")

        with allure.step("Enter Card Information"):
            self.signup.drp_card_type.select_by_index(4)
            self.signup.card_number.send_keys(Data.card)
            self.signup.drp_mm.select_by_index(10)
            self.signup.drp_yyyy.select_by_index(5)
            self.signup.cvv.send_keys(Data.cvv_code)
            self.signup.card_holder_name.send_keys(Data.reg_card_holder_name)
            self.signup.terms_conditions.click()
            with allure.step("Take Screenshot Card Information"):
                self.function.getScreenshot("CardInformation")

        with allure.step("Click submit"):
            self.signup.submit.click()

        with allure.step("Wait for registration"):
            self.function.WaitLocate(Locator.thank_you)

        with allure.step("Checking Successful registration"):
            self.function.TitleCheck("Account Information - SimpleTollFree")
            self.function.getScroll("200")
            self.function.getScreenshot("registration")
############################################################################################
        with allure.step("Take data for login"):
            self.SignUp_Toll = self.driver.find_element(By.XPATH, Locator.SignUp_Toll).text
            self.SignUp_Access = self.driver.find_element(By.XPATH, Locator.SignUp_Access).text
            self.SignUp_PIN = self.driver.find_element(By.XPATH, Locator.SignUp_PIN).text

        with allure.step("Checking email letter"):
            self.yandex.Autorization(Data.test_login, Data.test_password)

        with allure.step("Check letter"):
            self.yandex.CheckLetter()
            self.function.getScroll("400")

        with allure.step("Take Screenshot"):
            self.function.getScreenshot("letter_registation")

        with allure.step("Validation of information"):
            self.LOG_number = self.driver.find_element(By.XPATH, Locator.email_number).text
            self.LOG_access_code = self.driver.find_element(By.XPATH, Locator.email_access_code).text
            self.LOG_host_pin = self.driver.find_element(By.XPATH, Locator.email_host_pin).text
#############################################################################################
        with allure.step("Validation of letter registration"):
            assert self.SignUp_Toll == self.LOG_number
            assert self.SignUp_Access == self.LOG_access_code
            assert self.SignUp_PIN == self.LOG_host_pin

        with allure.step("Write data of new account"):
            subscription = open("subscriptions.txt", "a")
            subscription.write(str(datetime.date.today()))
            subscription.write("\n")
            subscription.write("Toll number : " + self.LOG_number + "\n")
            subscription.write("Access code : " + self.LOG_access_code + "\n")
            subscription.write("Host PIN : " + self.LOG_host_pin + "\n")
            subscription.write("\n")
            subscription.close()
        # with allure.step("Create subscription file"):
        #     allure.attach("subscriptions.txt")

        with allure.step("Clearing email"):
            self.yandex.EmptyEmail()
        with allure.step("Take Screenshot"):
            self.function.getScreenshot("clear")




    # @allure.suite("Registration")
    # @allure.feature("Checking registration letter")
    # @allure.description("Open yandex and check registration letter")
    # @allure.severity("Major")
    # def test_YandexLetterChecking(self):
    #     with allure.step("Open email page"):
    #         self.INIT()
    #     with allure.step("Checking email letter"):
    #         self.yandex.Autorization(Locator.test_login, Locator.test_password)
    #     with allure.step("Check letter"):
    #         self.yandex.CheckLetter()
    #         self.function.getScroll("400")
    #     with allure.step("Take Screenshot"):
    #         self.function.getScreenshot("letter_registation")
    #
    #
    #
    #     with allure.step("Clearing email"):
    #         self.yandex.EmptyEmail()
    #     with allure.step("Take Screenshot"):
    #         self.function.getScreenshot("clear")


