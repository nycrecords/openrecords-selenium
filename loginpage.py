import time
import unittest


class LoginPage(unittest.TestCase):
    admin_user = 'bwaite@records.nyc.gov'
    admin_pwd = 'Change4doris'

    agency_user = 'testthree@records.nyc.gov'
    agency_pwd = 'change4doris'

    public_user = 'john.doris0860@gmail.com'
    public_pwd = '31Ch@mbers'

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login(self, user_type):

        if user_type == "admin":
            self.driver.find_element_by_link_text("Log In").click()
            time.sleep(1)
            ##driver.find_element_by_id("Ecom_User_ID").clear()
            self.driver.find_element_by_id("employeeForm").submit()
            time.sleep(1)
            ##add email
            self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.admin_user)
            time.sleep(1)
            ##add password
            self.driver.find_element_by_id("Ecom_Password").send_keys(self.admin_pwd)
            time.sleep(1)
            form = self.driver.find_element_by_name("IDPLogin")
            time.sleep(1)
            form.submit()

            #check if user is currently logged on
            if self.driver.find_element_by_id("continue-current-session").is_displayed():
                self.driver.find_element_by_id("continue-current-session").click()
            else:
                pass

        elif user_type == "user":
            self.driver.find_element_by_link_text("Log In").click()
            time.sleep(1)
            ##driver.find_element_by_id("Ecom_User_ID").clear()
            self.driver.find_element_by_id("employeeForm").submit()
            time.sleep(1)
            ##add email
            self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.agency_user)
            time.sleep(1)
            ##add password
            self.driver.find_element_by_id("Ecom_Password").send_keys(self.agency_pwd)
            time.sleep(1)
            form = self.driver.find_element_by_name("IDPLogin")
            time.sleep(1)
            form.submit()

            #check if user is currently logged on
            if self.driver.find_element_by_id("continue-current-session").is_displayed():
                self.driver.find_element_by_id("continue-current-session").click()
            else:
                pass

        elif user_type == "public":
            self.driver.find_element_by_link_text("Log In").click()
            time.sleep(1)
            ##add email
            self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.public_user)
            time.sleep(1)
            ##add password
            self.driver.find_element_by_id("Ecom_Password").send_keys(self.public_pwd)
            time.sleep(1)
            form = self.driver.find_element_by_name("IDPLogin")
            time.sleep(1)
            form.submit()

            #check if user is currently logged on
            if self.driver.find_element_by_id("continue-current-session").is_displayed():
                self.driver.find_element_by_id("continue-current-session").click()
            else:
                pass

        else:
            pass
