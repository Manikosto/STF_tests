__author__ = 'Alexey Koledachkin'

import allure
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


from POM.Scripts.Tests_LoginPage import LoginPage
from POM.TestBase.EnvironmentSetUp import EnvironmentSetup
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from POM.locators import Locator
from POM.Data import Data
from POM.TestBase.Functions import Functions
from POM.Pages.LoginPage import Login
from POM.Pages.Account import Account
from POM.TestBase.Links import Links
from POM.Pages.Yandex import YandexLogin

class AccountPage(EnvironmentSetup):
 
###   INIT   ###

    def INIT(self):
        driver = self.driver
        self.driver.get(Links.account)
        self.locator = Locator()
        self.function = Functions(driver)
        self.login = Login(driver)
        self.account = Account(driver)
        self.data = Data()
        self.yandex = YandexLogin(driver)

    
    @allure.suite("Account information")
    @allure.title("Information")
    @allure.description("checking info on Account info page")
    @allure.severity("Major")
    def test_TollNumber(self):
        with allure.step("Opening page and logining"):
            self.INIT()
        with allure.step("Check Toll number"):
            assert self.account.Toll.text == self.data.Toll_number

        with allure.step("Check Toll-free number"):
            assert self.account.TollFree.text == self.data.correct_dial

        with allure.step("Check Access code"):
            assert self.account.acc_AccessCode.text == self.data.correct_access

        with allure.step("Check Host PIN"):
            assert self.account.acc_HostPIN.text == self.data.correct_pin

        with allure.step("Check Playback number"):
            assert self.account.acc_Playback_number.text == self.data.Playback_number

        with allure.step("Check First name"):
            assert self.account.acc_first_name.get_attribute("value") == self.data.prof_first_name

        with allure.step("Check Last name"):
            assert self.account.acc_last_name.get_attribute("value") == self.data.prof_last_name

        with allure.step("Check Email"):
            assert self.account.acc_email.get_attribute("value") == self.data.prof_email

        with allure.step("Check Phone number"):
            assert self.account.acc_phone_num.get_attribute("value") == self.data.prof_phone_number

        with allure.step("Check Company name"):
            assert self.account.acc_company_name.get_attribute("value") == self.data.prof_company_name

        with allure.step("Check Street address"):
            assert self.account.acc_street_address.get_attribute("value") == self.data.prof_address

        with allure.step("Check suite"):
            assert self.account.acc_suite.get_attribute("value") == self.data.prof_suite

        with allure.step("Check Zip"):
            assert self.account.acc_zip.get_attribute("value") == self.data.prof_zip

        with allure.step("Check State"):
            assert self.account.prof_state_locator.get_attribute("value") == self.data.prof_state

    @allure.suite("Account information")
    @allure.title("Time zone checking")
    @allure.description("checking time zone on Account info page")
    @allure.severity("Major")
    def test_TimeZone(self):
        with allure.step("Opening page and logining"):
            self.INIT()

        with allure.step("Show only USA time zones"):
            self.account.acc_change_zones.click()
            assert self.account.acc_change_zones.text == "Show all time zones"
            self.account.acc_time_click.click()
            time.sleep(1)
            self.function.getScreenshot("usazones")

        with allure.step("Show all time zones"):
            self.account.acc_change_zones.click()
            assert self.account.acc_change_zones.text == "Show U.S. only"
            self.account.acc_time_click.click()
            time.sleep(1)
            self.function.getScreenshot("allzones")


    @allure.suite("Account information")
    @allure.title("Resend info")
    @allure.description("checking info on Account info page")
    @allure.severity("Major")
    def test_ResendInfo(self):
        with allure.step("Opening page and logining"):
            self.INIT()

        with allure.step("Resend info"):
            self.account.acc_resend_info.click()
            self.function.WaitLocate(self.locator.resend_info_message)
            self.function.getScreenshot("resendinfo")

        with allure.step("Take data for login"):
            self.Login_Toll = self.account.Toll.text
            self.Login_Access = self.account.acc_AccessCode.text
            self.Login_PIN = self.account.acc_HostPIN.text

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

        with allure.step("Validation of letter registration"):
            assert self.Login_Toll == self.LOG_number
            assert self.Login_Access == self.LOG_access_code
            assert self.Login_PIN == self.LOG_host_pin

        with allure.step("Clearing email"):
            self.yandex.EmptyEmail()
        with allure.step("Take Screenshot"):
            self.function.getScreenshot("clear")