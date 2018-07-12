import time


class LoginPage:

    agency_user = 'gzhou@records.nyc.gov'
    agency_pwd = 'Change4me'

    def __init__(self, driver):
        self.driver = driver

    def test_login(self, user_type=""):
        self.driver.find_element_by_link_text("Log In").click()
        time.sleep(2)
        ##driver.find_element_by_id("Ecom_User_ID").clear()
        self.driver.find_element_by_id("employeeForm").submit()
        time.sleep(2)
        ##add email
        self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.agency_user)
        time.sleep(2)
        ##add password
        self.driver.find_element_by_id("Ecom_Password").send_keys(self.agency_pwd)
        time.sleep(2)
        form = self.driver.find_element_by_name("IDPLogin")
        time.sleep(2)
        form.submit()