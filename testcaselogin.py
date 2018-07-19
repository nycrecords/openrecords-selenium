from selenium import webdriver
import loginpage
import logoutpage
import requestrecordpage
import unittest
import sys
import nypdrequest
import time
import publicrequestpage


class LoginTest(unittest.TestCase):
    user_type = ''

    def test_login(self):
        #self.driver = webdriver.Chrome('C:\\Users\\bwaite\\Drivers\\chromedriver.exe')
        self.driver = webdriver.Chrome('/Users/bzhuang/Downloads/chromedriver')
        self.driver.get("https://openrecords-test.appdev.records.nycnet/")
        #self.driver.get("https://a860-openrecords.csc.nycnet/")

        log_in = loginpage.LoginPage(self.driver)
        log_in.login(self.user_type)
        time.sleep(1)

    
        #request = requestrecordpage.RequestPage(self.driver)
        #request.request(self.user_type)
        
        # request = publicrequestpage.RequestPage(self.driver)
        # request.agency_request(self.user_type)

        request = nypdrequest.nypdrequest(self.driver)
        request.nypdrequestfun(self.user_type)


        logout = logoutpage.LogoutPage(self.driver)
        logout.logout(self.user_type)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        LoginTest.user_type = sys.argv.pop()
    unittest.main()
