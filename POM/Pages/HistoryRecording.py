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
from POM.Pages.LoginPage import Login
from POM.Data import Data
from POM.TestBase.Links import Links

# driver.find_element(By.XPATH(''))
class History():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.login = Login(driver)
###   Locators   ###
        self.function = Functions(driver)

        self.LoggingIn()
        self.driver.get(Links.recordings)

        self.start_date = self.driver.find_element(By.XPATH, Locator.start_date)
        self.end_date = self.driver.find_element(By.XPATH, Locator.end_date)
        self.type_conference = Select(self.driver.find_element(By.XPATH, Locator.type_conference))
        self.search = self.driver.find_element(By.XPATH, Locator.search)

        ### Sorting
        self.sort_by_date_time = self.driver.find_element(By.XPATH, Locator.sort_by_date_time)
        self.sort_by_end_time = self.driver.find_element(By.XPATH, Locator.sort_by_end_time)
        self.sort_by_callers = self.driver.find_element(By.XPATH, Locator.sort_by_callers)
        self.sort_by_duration = self.driver.find_element(By.XPATH, Locator.sort_by_duration)
        self.sort_by_recording_options = self.driver.find_element(By.XPATH, Locator.sort_by_recording_options)
        self.sort_by_size = self.driver.find_element(By.XPATH, Locator.sort_by_size)

        ### Work with table
        self.open_recording = self.driver.find_element(By.XPATH, Locator.open_recording)

        self.download = self.driver.find_element(By.XPATH, Locator.download)
        self.play = self.driver.find_element(By.XPATH, Locator.play)
        self.trash = self.driver.find_element(By.XPATH, Locator.trash)

    def LoggingIn(self):
        self.login.dial_number.send_keys(Data.correct_dial)
        self.login.accesscode.send_keys(Data.correct_access)
        self.login.host_pin.send_keys(Data.correct_pin)
        self.login.remember_me.click()
        self.login.submit.click()
        self.function.WaitLocate(Locator.page_name)
        self.function.getScreenshot("login")
        self.function.TitleCheck(Locator.login_title)


