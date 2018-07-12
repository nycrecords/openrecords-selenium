import time


class LoginPage:
    username = 'bwaite@records.nyc.gov'
    pwd = 'Change4doris'

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        self.driver.find_element_by_link_text("Log In").click()
        time.sleep(2)
        ##driver.find_element_by_id("Ecom_User_ID").clear()
        self.driver.find_element_by_id("employeeForm").submit()
        time.sleep(2)
        ##add email
        self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.username)
        time.sleep(2)
        ##add password
        self.driver.find_element_by_id("Ecom_Password").send_keys(self.pwd)
        time.sleep(2)
        ##driver.find_element_by_id("login").click()
        ##driver.find_element_by_xpath("//button[@type='button']").click()
        form = self.driver.find_element_by_name("IDPLogin")
        time.sleep(2)
        form.submit()