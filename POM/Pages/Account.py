__author__ = 'Alexey Koledachkin'

import unittest
import allure
import pytest
import selenium
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.locators import Locator
from POM.Data import Data
from POM.TestBase.Functions import Functions
from POM.Pages.LoginPage import Login

# driver.find_element(By.XPATH(''))
class Account():

    ###   Pre-condition   ###
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.function = Functions(driver)
        self.login = Login(driver)
        self.data = Data()
        ###   Loggining   ###
        self.LoggingIn()

        ###   Locators   ###
        self.acc_email = self.driver.find_element(By.XPATH, Locator.acc_email)
        self.submit = self.driver.find_element(By.XPATH, Locator.submit)
        self.acc_first_name = self.driver.find_element(By.XPATH, Locator.first_name)
        self.acc_last_name = self.driver.find_element(By.XPATH, Locator.acc_last_name)
        self.acc_phone_num = self.driver.find_element(By.XPATH, Locator.acc_phone_num)
        self.acc_company_name = self.driver.find_element(By.XPATH, Locator.acc_company_name)

        self.acc_street_address = self.driver.find_element(By.XPATH, Locator.acc_street_address)
        self.acc_suite = self.driver.find_element(By.XPATH, Locator.acc_suite)
        self.acc_city = self.driver.find_element(By.XPATH, Locator.acc_city)
        self.acc_zip = self.driver.find_element(By.XPATH, Locator.acc_zip)
        self.drp_state = Select(self.driver.find_element(By.XPATH, Locator.acc_state))  # SELECT

        self.Toll = self.driver.find_element(By.XPATH, Locator.Toll)
        self.TollFree = self.driver.find_element(By.XPATH, Locator.TollFree)
        self.acc_AccessCode = self.driver.find_element(By.XPATH, Locator.acc_AccessCode)
        self.acc_HostPIN = self.driver.find_element(By.XPATH, Locator.acc_HostPIN)
        self.acc_Playback_number = self.driver.find_element(By.XPATH, Locator.acc_Playback_number)
        self.prof_state_locator = self.driver.find_element(By.XPATH, Locator.prof_state_locator)

        self.drp_timezone = Select(self.driver.find_element(By.XPATH, Locator.acc_timezones))
        self.acc_time_click = self.driver.find_element(By.XPATH, Locator.acc_timezones) # For click
        self.acc_change_zones = self.driver.find_element(By.XPATH, Locator.acc_change_zones)
        self.acc_resend_info = self.driver.find_element(By.XPATH, Locator.acc_resend_info)

    ###   Functions   ###
    def LoggingIn(self):
        self.login.dial_number.send_keys(Data.correct_dial)
        self.login.accesscode.send_keys(Data.correct_access)
        self.login.host_pin.send_keys(Data.correct_pin)
        self.login.remember_me.click()
        self.login.submit.click()
        self.function.WaitLocate(Locator.page_name)
        self.function.getScreenshot("login")
        self.function.TitleCheck(Locator.login_title)