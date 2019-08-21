__author__ = 'Alexey Koledachkin'

import allure
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


from POM.Scripts.Tests_LoginPage import LoginPage
from POM.TestBase.EnvironmentSetUp import EnvironmentSetup
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from POM.locators import Locator
from POM.Data import Data
from POM.TestBase.Functions import Functions
from POM.Pages.LoginPage import Login
from POM.Pages.HistoryRecording import History
from POM.Pages.Account import Account
from POM.TestBase.Links import Links
from POM.Pages.Yandex import YandexLogin

class HistoryRecording(EnvironmentSetup):

###   INIT   ###

    def INIT(self):
        driver = self.driver

        self.driver.get(Links.account)

        self.login = Login(driver)
        self.function = Functions(driver)

        self.history = History(driver)
        self.locator = Locator()
        self.data = Data()

    @allure.suite("History and Recordings")
    @allure.title("Open recording")
    @allure.description("Checking opening of recordings on Recordings page")
    @allure.severity("Major")
    def test_OpenRecording(self):
        with allure.step("Opening page and logining"):
            self.INIT()

        with allure.step("Checking title"):
            self.function.TitleCheck(Locator.recordings)

        with allure.step("Open recording"):
            self.history.open_recording.click()

        with allure.step("Checking correct opening of record"):
            assert self.history.open_recording.get_attribute("class") == "fa fa-minus icon-minus"
            self.function.getScreenshot("openrecord")

        with allure.step("Close record"):
            self.driver.find_element(By.XPATH, Locator.close_recording).click()
            self.function.getScreenshot("closerecord")

    # @allure.suite("History and Recordings")
    # @allure.title("Open recording")
    # @allure.description("Checking opening of recordings on Recordings page")
    # @allure.severity("Major")
    # def test_OpenRecording(self):
    #     with allure.step("Opening page and logining"):
    #         self.INIT()
    #     with allure.step("Checking title"):
    #         self.function.TitleCheck(Locator.recordings)
    #     with allure.step("Open recording"):
    #         self.history.open_recording.click()
    #     with allure.step("Checking correct opening of record"):
    #         assert self.history.open_recording.get_attribute("class") == "fa fa-minus icon-minus"
    #     with allure.step(""):
    #         self.function.getScreenshot("openrecord")
    #