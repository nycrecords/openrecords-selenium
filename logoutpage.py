import time


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self, user_type):
        if user_type == "admin" or user_type == "user" or user_type == "public":
            self.driver.find_element_by_id("logout").click()
            time.sleep(3)
        else:
            pass
