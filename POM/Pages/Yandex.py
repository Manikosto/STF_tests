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

# driver.find_element(By.XPATH(''))
class YandexLogin():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Autorization(self, login, password):
        self.driver.get("https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")
        self.driver.find_element(By.XPATH, Locator.test_login_email).send_keys(login)
        self.driver.find_element(By.XPATH, Locator.test_submit_button).click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.test_password_email)))
            self.driver.find_element(By.XPATH, Locator.test_password_email).send_keys(password)
            self.driver.find_element(By.XPATH, Locator.test_submit_button).click()
        except:
            pass

    def CheckLetter(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='SimpleTollFree.com Account Registration']")))
            self.driver.find_element(By.XPATH, "//span[text()='SimpleTollFree.com Account Registration']").click()
            self.pin_letter = self.driver.find_element(By.XPATH, Locator.pin_letter)
            self.pin_letter = self.pin_letter.text

        except:
            pass

    def EmptyEmail(self):
        self.driver.back()
        self.driver.find_element(By.XPATH, Locator.checkbox_clear).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.delete)))
        self.driver.find_element(By.XPATH, Locator.delete).click()
        time.sleep(3)








