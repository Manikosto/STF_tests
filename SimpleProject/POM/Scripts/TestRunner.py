from unittest import TestLoader, TestSuite, TextTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POM.Scripts.Tests_ContactUs import ContactPage
from POM.Scripts.Tests_HomePage import HomePage
from POM.Scripts.Tests_LoginPage import LoginPage
from POM.Scripts.Tests_SignUp import SignUpPage
from POM.Scripts.Tests_AccountPage import AccountPage



if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ContactPage),
        loader.loadTestsFromTestCase(HomePage),
        loader.loadTestsFromTestCase(LoginPage),
        loader.loadTestsFromTestCase(SignUpPage),
        loader.loadTestsFromTestCase(AccountPage)
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

