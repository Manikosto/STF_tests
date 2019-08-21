__author__ = 'Alexey Koledachkin'

import allure
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POM.Pages.ContactUs import ContactUs
from POM.TestBase.EnvironmentSetUp import EnvironmentSetup
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from POM.locators import Locator
from POM.TestBase.Functions import Functions
from POM.TestBase.Links import Links


class ContactPage(EnvironmentSetup):

###   INIT   ###

    def INIT(self):
        driver = self.driver
        self.driver.get(Links.contact_us)
        self.contact = ContactUs(driver)
        self.function = Functions(driver)
        self.locator = Locator()

###   Tests   ###

    # Send form from Participant to Support
    @allure.suite("ContactPage checking")
    @allure.title("Send form")
    @allure.description("Open ContactUs page and send form")
    @allure.severity("Trivial")
    def test_SendForm(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Title cheking
        with allure.step("Title cheking"):
            self.function.TitleCheck("Contact Us - SimpleTollFree")
        # Enter info in fields
        with allure.step("Enter info in fields"):
            self.contact.SendForm("Test", "lol@gmail.com", "89999999999", "Hello")
            time.sleep(4)
        # Take screenshot
        with allure.step("Take screenshot"):
            self.function.getScreenshot("Screen")


    # Checking required fields
    @allure.suite("ContactPage checking")
    @allure.title("Required fields checking")
    @allure.description("Check form on required fields")
    @allure.severity("Major")
    def test_RequiredFields(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Title checking
        with allure.step("Title checking"):
            self.function.TitleCheck("Contact Us - SimpleTollFree")
        # Click to Submit button
        with allure.step("Click to Submit button"):
            self.contact.submit.click()
            time.sleep(5)
        # Required fields checking
        with allure.step("Required fields checking"):
            try:
                with allure.step("Find label of required field"):
                    self.function.WaitLocate(Locator.r_field)
                with allure.step("Find label of required field"):
                    self.function.getScreenshot("requiredFields")
            except:
                print("No main fields")


    # Checking format of Name fields
    @allure.suite("ContactPage checking")
    @allure.title("Name field format")
    @allure.description("Check form on right format of fields")
    @allure.severity("Minor")
    def test_NameFormat(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Checking Name field
        with allure.step("Checking Name field"):
            self.contact.name.send_keys("      ")
        # Write correct form
        with allure.step("Write correct form"):
            self.contact.email.send_keys("test@gmail.com")
            self.contact.phone.send_keys("89999999999")
            self.contact.comments.send_keys("Hello World")
        # Send incorrect form
        with allure.step("Send incorrect form"):
            self.contact.submit.click()
            self.function.WaitLocate(self.locator.r_field)
            self.function.ElementSelection(self.locator.r_field)
        # Take screenshot
        with allure.step("Take screenshot"):
            self.function.getScreenshot("Name")


    # Checking format of Email fields
    @allure.suite("ContactPage checking")
    @allure.title("Email field format")
    @allure.description("Check form on right format of fields")
    @allure.severity("Minor")
    def test_EmailFormat(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Checking Email field
        with allure.step("Checking Email field"):
            self.contact.email.send_keys("testfgshf.fy")
        # Write correct form
        with allure.step("Write correct form"):
            self.contact.name.send_keys("Test")
            self.contact.phone.send_keys("89999999999")
            self.contact.comments.send_keys("Hello World")
        # Send incorrect form
        with allure.step("Send incorrect form"):
            self.contact.submit.click()
            self.function.WaitLocate(self.locator.invalid_mail)
            self.function.ElementSelection(self.locator.invalid_mail)
        # Take screenshot
        with allure.step("Take screenshot"):
            self.function.getScreenshot("Email")


    # Checking format of Phone fields
    @allure.suite("ContactPage checking")
    @allure.title("Phone field format")
    @allure.description("Check form on right format of fields")
    @allure.severity("Minor")
    def test_PhoneFormat(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()
        # Checking Phone field
        with allure.step("Checking Phone field"):
            self.contact.phone.send_keys("8999999")
        # Write correct form
        with allure.step("Write correct form"):
            self.contact.name.send_keys("Test")
            self.contact.email.send_keys("test@gmail.com")
            self.contact.comments.send_keys("Hello World")
        # Send incorrect form
        with allure.step("Send incorrect form"):
            self.contact.submit.click()
            self.function.WaitLocate(self.locator.invalid_number)
            self.function.ElementSelection(self.locator.invalid_number)
        # Take screenshot
        with allure.step("Take screenshot"):
            self.function.getScreenshot("Phone")


    # Social link checking
    @allure.suite("ContactPage checking")
    @allure.title("Social links")
    @allure.description("Social links checking")
    @allure.severity("Trivial")
    def test_SocialLinks(self):
        # Open page in the browser
        with allure.step("Open page in the browser"):
            self.INIT()

        '''   RSS page checking   '''

        with allure.step("Checking title of COntact Us page"):
            self.function.TitleCheck("Contact Us - SimpleTollFree")

        with allure.step("Click on RSS link"):
            self.function.getClick(self.locator.rss)

        with allure.step("Take screenshot of FCC Blog page"):
            self.function.getScreenshot("RSS")

        '''   Youtube page checking   '''

        with allure.step("Back to Contact Us page"):
            self.driver.back()

        with allure.step("Click on Youtube link"):
            self.function.getClick(self.locator.youtube)

        with allure.step("Take screenshot of Youtube page FCC"):
            self.function.getScreenshot("Youtube")

        '''   Facebook page checking   '''

        with allure.step("Back to Contact Us page"):
            self.driver.back()

        with allure.step("Click on Youtube link"):
            self.function.getClick(self.locator.facebook)

        with allure.step("Take screenshot of Facebook FCC page"):
            self.function.getScreenshot("Facebook")

        '''   Twitter page checking   '''

        with allure.step("Back to Contact Us page"):
            self.driver.back()

        with allure.step("Click on Twitter link"):
            self.function.getClick(self.locator.twitter)

        with allure.step("Take screenshot of Twitter FCC page"):
            self.function.getScreenshot("Twitter")


    # # Test
    # @allure.feature("Element Selection")
    # @allure.story("Test")
    # @allure.severity("Trivial")
    # def test_some(self):
    #
    #     with allure.step("Open page in browser"):
    #         self.INIT()
    #
    #     with allure.step("Title checking"):
    #         self.function.TitleCheck("Contact Us - SimpleTollFree")
    #
    #     with allure.step("Find element"):
    #         self.function.ElementSelection(Locator.faq)
    #         self.function.getScreenshot("ElementNotFound")
    #
    #     with allure.step("Click on element"):
    #         self.contact.faq.click()







###   Report   ###

