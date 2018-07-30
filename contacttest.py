from selenium import webdriver
import loginpage
import logoutpage
import requestrecordpage
import unittest
import sys
import nypdrequest
import time
import publicrequestpage
import contactagency


class ContactTest(unittest.TestCase):
    user_type = ''

    def test_login(self):
        #self.driver = webdriver.Chrome('C:\\Users\\bwaite\\Drivers\\chromedriver.exe')
        self.driver = webdriver.Chrome('/Users/bzhuang/Downloads/chromedriver')
        self.driver.get("https://openrecords-test.appdev.records.nycnet/")
        #self.driver.get("https://a860-openrecords.csc.nycnet/")

        log_in = loginpage.LoginPage(self.driver)
        log_in.login(self.user_type)
        time.sleep(1)

    
        contact = contactagency.ContactAgency(self.driver)
        contact.contact(self.user_type)

        logout = logoutpage.LogoutPage(self.driver)
        logout.logout(self.user_type)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ContactTest.user_type = sys.argv.pop()
    unittest.main()