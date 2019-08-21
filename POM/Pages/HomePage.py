__author__ = 'Alexey Koledachkin'

import unittest
import allure
import pytest
import selenium
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.locators import Locator
from selenium.webdriver.support.ui import WebDriverWait

class Home():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
###   Locators   ###
        self.logo = self.driver.find_element(By.XPATH, Locator.logo)
        self.sign_up = self.driver.find_element(By.XPATH, Locator.sign_up)
        self.login = self.driver.find_element(By.XPATH, Locator.login)
        self.home_p = self.driver.find_element(By.XPATH, Locator.home)
        self.contact_us = self.driver.find_element(By.XPATH, Locator.contact_us)
        self.faq = self.driver.find_element(By.XPATH, Locator.faq)
        self.about_us = self.driver.find_element(By.XPATH, Locator.about_us)
        self.home_bottom = self.driver.find_element(By.XPATH, Locator.home_bottom)
        self.contact_bottom = self.driver.find_element(By.XPATH, Locator.contact_bottom)
        self.faq_bottom = self.driver.find_element(By.XPATH, Locator.faq_bottom)
        self.about_bottom = self.driver.find_element(By.XPATH, Locator.about_bottom)




    '''   Functions of Home Page   '''
    ###   Finctions   ###


















