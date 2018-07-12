from selenium import webdriver
import publicloginpage
import publicrequestpage
import unittest


class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        self.driver = webdriver.Chrome('C:\\Selenium\\chromedriver.exe')
        #self.driver.get("https://openrecords-test.appdev.records.nycnet/")
        self.driver.get("https://a860-openrecords.csc.nycnet/")
        log_in = publicloginpage.LoginPage(self.driver)
        log_in.test_login()

        request = publicrequestpage.RequestPage(self.driver)
        request.agency_request()


    #def tearDown(self):
    #    self.driver.quit()


if __name__ == "__main__":
    unittest.main()