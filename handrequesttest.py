from selenium import webdriver
import loginpage
import logoutpage
import requestrecordpage
import unittest
import sys
import time
import handlerequest

class HandleRequests(unittest.TestCase):
    def test_handle(self):
        #self.driver = webdriver.Chrome('C:\\Users\\bwaite\\Drivers\\chromedriver.exe')
        self.driver = webdriver.Chrome('/Users/bzhuang/Downloads/chromedriver')
        self.driver.get("https://openrecords-test.appdev.records.nycnet/")
        #self.driver.get("https://a860-openrecords.csc.nycnet/")

        log_in = loginpage.LoginPage(self.driver)
        log_in.login(self.user_type)
        time.sleep(1)

        handle = handlerequest.HandleRequest(self.driver)
        handle.handle_request(self.user_type)

        logout = logoutpage.LogoutPage(self.driver)
        logout.logout(self.user_type)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        HandleRequests.user_type = sys.argv.pop()
    unittest.main()
