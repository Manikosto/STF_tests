__author__ = 'Alexey Koledachkin'

from selenium.webdriver.common.by import By
from POM.locators import Locator
from POM.TestBase.Functions import Functions

# driver.find_element(By.XPATH(''))
class Login():
    def __init__(self, driver):
        self.driver = driver
        self.function = Functions(driver)
###   Locators   ###
        self.logo = self.driver.find_element(By.XPATH, Locator.logo)
        self.sign_up = self.driver.find_element(By.XPATH, Locator.sign_up)
        self.login = self.driver.find_element(By.XPATH, Locator.login)
        self.home = self.driver.find_element(By.XPATH, Locator.home)
        self.contact_us = self.driver.find_element(By.XPATH, Locator.contact_us)
        self.faq = self.driver.find_element(By.XPATH, Locator.faq)
        self.about_us = self.driver.find_element(By.XPATH, Locator.about_us)
        self.home_bottom = self.driver.find_element(By.XPATH, Locator.home_bottom)
        self.contact_bottom = self.driver.find_element(By.XPATH, Locator.contact_bottom)
        self.faq_bottom = self.driver.find_element(By.XPATH, Locator.faq_bottom)
        self.about_bottom = self.driver.find_element(By.XPATH, Locator.about_bottom)

        self.dial_number = self.driver.find_element(By.XPATH, Locator.dial_number)
        self.accesscode = self.driver.find_element(By.XPATH, Locator.accesscode)
        self.host_pin = self.driver.find_element(By.XPATH, Locator.host_pin)
        self.remember_me = self.driver.find_element(By.XPATH, Locator.remember_me)
        self.submit = self.driver.find_element(By.XPATH, Locator.submit)
        self.forgot_pass = self.driver.find_element(By.XPATH, Locator.forgot_pass)
        self.send_info = self.driver.find_element(By.XPATH, Locator.send_info)


    def LoginIn(self, number, code, pin):
        self.login.dial_number.send_keys(number)
        self.login.accesscode.send_keys(code)
        self.login.host_pin.send_keys(pin)
        self.login.remember_me.click()
        self.login.submit.click()
        self.function.WaitLocate(Locator.page_name)
        self.function.getScreenshot("login")
        self.function.TitleCheck(Locator.login_title)