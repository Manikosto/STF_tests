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

# driver.find_element(By.XPATH(''))
class ContactUs():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
###   Locators   ###

        self.name = self.driver.find_element(By.XPATH, Locator.name)
        self.email = self.driver.find_element(By.XPATH, Locator.email)
        self.phone = self.driver.find_element(By.XPATH, Locator.phone)
        self.comments = self.driver.find_element(By.XPATH, Locator.comments)
        self.submit = self.driver.find_element(By.XPATH, Locator.submit)

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

        self.rss = self.driver.find_element(By.XPATH, Locator.rss)
        self.facebook = self.driver.find_element(By.XPATH, Locator.facebook)
        self.youtube = self.driver.find_element(By.XPATH, Locator.youtube)
        self.twitter = self.driver.find_element(By.XPATH, Locator.twitter)



    def setName(self, Name):
        assert self.name
        self.name.clear()
        self.name.send_keys(Name)

    def setEmail(self,Email):
        assert self.name
        self.email.clear()
        self.email.send_keys(Email)

    def setPhone(self,Phone):
        assert self.name
        self.phone.clear()
        self.phone.send_keys(Phone)

    def setComment(self,Comment):
        assert self.name
        self.comments.clear()
        self.comments.send_keys(Comment)

    def getSubmit(self):
        assert self.name
        return self.submit




        ###   Functions   ###

    def SendForm(self, name, email, phone, comment):
        driver = self.driver
        contact = ContactUs(driver)
        contact.setName(name)
        contact.setEmail(email)
        contact.setPhone(phone)
        contact.setComment(comment)
        contact.submit.click()



