import unittest
import allure
import pytest
import selenium
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType
from POM.locators import Locator


class Functions():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    # Function for title checking
    def TitleCheck(self, title):
        try:
            assert self.driver.title == title
        except AssertionError:
            self.driver.close()
            self.driver.quit()

    # Click function, it help avoid error
    def getClick(self,element):
        self.ElementSelection(element)
        elem = self.driver.find_element(By.XPATH, element).click()
        if elem != elem:
            return False


    # Select Element
    def ElementSelection(self,xpath):
        # self.driver.execute_script("function getElementByXpath(path) {return document.evaluate(path,document,null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}console.log((getElementByXpath(\""+xpath+"\").style.backgroundColor='#fff'));")
        try:
            self.driver.execute_script("function getElementByXpath(path) {return document.evaluate(path,document,null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}console.log((getElementByXpath(\""+xpath+"\").style.border=\"3px solid #0cff00\"));")
        except:
            print("Element have not found")
            self.driver.close()

    # Wait for locate
    def WaitLocate(self, xpath):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        self.ElementSelection(xpath)

    # Screenshot for Allure
    def getScreenshot(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

    # Scroll down
    def getScroll(self, px):
        self.driver.execute_script("window.scrollTo(0,"+px+")")

    # Find element
    def getElement(self, elem):
        self.driver.find_element(By.XPATH, elem)

    def OpenBrowser(self, page):
        self.driver.get(page)