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
from POM.locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from POM.TestBase.Functions import Functions

# driver.find_element(By.XPATH(''))
class SignUp():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
###   Locators   ###
        self.function = Functions(driver)
        self.email = self.driver.find_element(By.XPATH, Locator.email)
        self.submit = self.driver.find_element(By.XPATH, Locator.submit)
        self.first_name = self.driver.find_element(By.XPATH, Locator.first_name)
        self.last_name = self.driver.find_element(By.XPATH, Locator.last_name)
        self.phone_num = self.driver.find_element(By.XPATH, Locator.phone_num)
        self.company_name = self.driver.find_element(By.XPATH, Locator.company_name)
        self.card_number = self.driver.find_element(By.XPATH, Locator.card_number)
        self.cvv = self.driver.find_element(By.XPATH, Locator.cvv)
        self.card_holder_name = self.driver.find_element(By.XPATH, Locator.card_holder_name)
        self.terms_conditions = self.driver.find_element(By.XPATH, Locator.terms_conditions)
        self.street_address = self.driver.find_element(By.XPATH, Locator.street_address)
        self.suite = self.driver.find_element(By.XPATH, Locator.suite)
        self.city = self.driver.find_element(By.XPATH, Locator.city)
        self.zip = self.driver.find_element(By.XPATH, Locator.zip)
        self.same_above = self.driver.find_element(By.XPATH, Locator.same_above)
        self.login = self.driver.find_element(By.XPATH, Locator.login)

        self.drp_card_type=Select(self.driver.find_element(By.XPATH, Locator.card_type)) # SELECT
        self.drp_mm = Select(self.driver.find_element(By.XPATH, Locator.mm))  # SELECT
        self.drp_yyyy = Select(self.driver.find_element(By.XPATH, Locator.yyyy))  # SELECT
        self.drp_state = Select(self.driver.find_element(By.XPATH, Locator.state))  # SELECT

        self.base_page = "https://www.simpletollfree.com/signup"



    def LoginIn(self, number, code, pin):
        self.login = self.driver.find_element(By.XPATH, Locator.login)
        self.login.dial_number.send_keys(number)
        self.login.accesscode.send_keys(code)
        self.login.host_pin.send_keys(pin)
        self.login.remember_me.click()
        self.login.submit.click()
        self.function.WaitLocate(Locator.page_name)
        self.function.getScreenshot("login")
        self.function.TitleCheck(Locator.login_title)



