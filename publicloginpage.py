import time


class LoginPage:

    public_user = 'john.doris0860@gmail.com'
    public_pwd = '31Ch@mbers'

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
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