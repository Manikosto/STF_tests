__author__ = 'Alexey Koledachkin'

import allure
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POM.TestBase.EnvironmentSetUp import EnvironmentSetup
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.locators import Locator
from POM.TestBase.Functions import Functions
from POM.Pages.HomePage import Home
from POM.TestBase.Links import Links

class HomePage(EnvironmentSetup):

    def INIT(self):
        driver = self.driver
        self.driver.get(Links.home)
        self.home = Home(driver)
        self.function = Functions(driver)
        self.locator = Locator()

        ###   Functions   ###

    # Checking navigations
    @allure.suite("HomePage checking")
    @allure.title("Navigations checking")
    @allure.description("Open Home page and checking top menu")
    @allure.severity("Critical")
    def test_TopMenuChecking(self):

        with allure.step("Open page in the browser"):
            self.INIT()

        '''   Go to About Us page   '''

        with allure.step("Go to About Us page"):
            self.function.getClick(self.locator.about_us)

        with allure.step("Checking title of About Us page"):
            self.function.TitleCheck("About Us - SimpleTollFree")
            self.driver.back()

        '''   Go to Contact Us page   '''

        with allure.step("Go to Contact Us page"):
            self.function.getClick(self.locator.contact_us)
        with allure.step("Checking title of Contact Us"):
            self.function.TitleCheck("Contact Us - SimpleTollFree")
            self.driver.back()

        '''   Go to FAQ page   '''

        with allure.step("Go to FAQ page"):
            self.function.getClick(self.locator.faq)
        with allure.step("Checking title of FAQ page"):
            self.function.TitleCheck("FAQ - SimpleTollFree")

        '''   Go to Home page   '''

        with allure.step("Go to Home page"):
            self.function.getClick(self.locator.home)
        with allure.step("Checking title of Home page"):
            self.function.TitleCheck("Toll Free Conferencing – Simple Toll Free Conferencing")


    # Checking bottom navigations
    @allure.suite("HomePage checking")
    @allure.title("Bottom navigations checking")
    @allure.description("Open Home page and checking bottom menu")
    @allure.severity("Critical")
    def test_BottomMenuChecking(self):

        with allure.step("Open page in the browser"):
            self.INIT()

        '''   Go to About Us page   '''

        with allure.step("Go to About Us page"):
            self.function.getClick(self.locator.about_bottom)
        with allure.step("Checking title of About Us page"):
            self.function.TitleCheck("About Us - SimpleTollFree")
            self.driver.back()

        '''   Go to Contact Us page   '''

        with allure.step("Go to Contact Us page"):
            self.function.getClick(self.locator.contact_bottom)
        with allure.step("Checking title of Contact Us"):
            self.function.TitleCheck("Contact Us - SimpleTollFree")
            self.driver.back()

        '''   Go to FAQ page   '''

        with allure.step("Go to FAQ page"):
            self.function.getClick(self.locator.faq_bottom)
        with allure.step("Checking title of FAQ page"):
            self.function.TitleCheck("FAQ - SimpleTollFree")
            self.driver.back()

        '''   Go to Home page   '''

        with allure.step("Go to Home page"):
            self.function.getClick(self.locator.home_bottom)
        with allure.step("Checking title of Home page"):
            self.function.TitleCheck("Toll Free Conferencing – Simple Toll Free Conferencing")


    # Checking sign up button
    @allure.suite("HomePage checking")
    @allure.title("SignUp button")
    @allure.description("Open Home page and checking SignUp button")
    @allure.severity("Critical")
    def test_SignUpButton(self):

        with allure.step("Open page in the browser"):
            self.INIT()

        with allure.step("Go to Sign Up page"):
            self.function.getClick(self.locator.sign_up)
        with allure.step("Checking title of Registration page"):
            self.function.TitleCheck("Registration Page - SimpleTollFree")
            self.function.getScreenshot("SignUp")

    # Checking login button
    @allure.suite("HomePage checking")
    @allure.title("Login button")
    @allure.description("Open Home page and checking Login button")
    @allure.severity("Critical")
    def test_LoginButton(self):
        with allure.step("Open page in the browser"):
            self.INIT()

        with allure.step("Go to Login page"):
            self.function.getClick(self.locator.login)
        with allure.step("Checking title of Login page"):
            self.function.TitleCheck("Login - SimpleTollFree")
            self.function.getScreenshot("Login")


    # Checking Logo link
    @allure.suite("HomePage checking")
    @allure.title("Logo Link")
    @allure.description("Open Home page and checking LogoLink")
    @allure.severity("Trivial")
    def test_LogoLink(self):
        with allure.step("Open page in the browser"):
            self.INIT()
        with allure.step("Checking Logo"):
            self.function.ElementSelection(self.locator.logo)
            self.function.getClick(self.locator.logo)
            self.function.TitleCheck("Toll Free Conferencing – Simple Toll Free Conferencing")


