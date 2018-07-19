from selenium import webdriver
import loginpage
import agencyrequestpage
import sys
import unittest


class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        self.driver = webdriver.Chrome('C:\\Selenium\\chromedriver.exe')
        self.driver.get("https://openrecords-test.appdev.records.nycnet/")
        #self.driver.get("https://a860-openrecords.csc.nycnet/")
        log_in = loginpage.LoginPage(self.driver)
        log_in.login()

        request = agencyrequestpage.RequestPage(self.driver)
        request.agency_request()


    #def tearDown(self):
    #    self.driver.quit()


if __name__ == "__main__":
    unittest.main()