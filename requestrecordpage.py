from selenium.webdriver.support.ui import Select
from testcaselogin import LoginTest
import time


class RequestPage(LoginTest):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def request(self, user_type):

        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Request a Record").click()
            time.sleep(1)

            form = self.driver.find_element_by_id("submit")
            time.sleep(1)
            form.submit()

            self.assertTrue(self.driver.find_element_by_id("parsley-id-7"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-9"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-13"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-17"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-19"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-21"))

            self.driver.find_element_by_id("request-title").send_keys(
                "A request title can only be 90 characters in length. A request title can only be 90 charac100")
            time.sleep(1)

            self.assertTrue(self.driver.find_element_by_id("title-character-count"))

            self.driver.find_element_by_id("request-title").clear()
            self.driver.find_element_by_id("request-title").send_keys("TEST REQUEST TITLE")
            time.sleep(1)

            # self.driver.find_element_by_id("request-description").send_keys("This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is100")
            # time.sleep(1)

            self.assertTrue(self.driver.find_element_by_id("description-character-count"))

            self.driver.find_element_by_id("request-description").clear()
            self.driver.find_element_by_id("request-description").send_keys("TEST REQUEST DESCRIPTION")
            time.sleep(1)

            self.driver.find_element_by_id("request-file").send_keys("Q:\\Projects\\OpenRecords\\test_files\\Test1.docx")
            time.sleep(1)

            select = Select(self.driver.find_element_by_id("method-received"))
            select.select_by_value("Email")
            time.sleep(1)

            self.driver.find_element_by_id("first-name").send_keys("John")
            time.sleep(1)

            self.driver.find_element_by_id("last-name").send_keys("Doris")
            time.sleep(1)

            self.driver.find_element_by_id("email").send_keys("john.doris0860@gmail.com")
            time.sleep(1)

            self.driver.find_element_by_id("user-title").send_keys("User's Title")
            time.sleep(1)

            self.driver.find_element_by_id("user-organization").send_keys("User's Organization")
            time.sleep(1)

            self.driver.find_element_by_id("phone").send_keys("5555555555")
            time.sleep(1)

            self.driver.find_element_by_id("fax").send_keys("5555555555")
            time.sleep(1)

            self.driver.find_element_by_id("address-line-1").send_keys("123 Main Street")
            time.sleep(1)

            self.driver.find_element_by_id("address_two").send_keys("Apt 3D")
            time.sleep(1)

            self.driver.find_element_by_id("city").send_keys("New York")
            time.sleep(1)

            self.driver.find_element_by_id("zipcode").send_keys("12345")
            time.sleep(1)

            form = self.driver.find_element_by_name("submit")
            form.submit()
            time.sleep(1)

            self.assertTrue(self.driver.find_element_by_class_name("alert-success"))

        elif user_type == "public":
            self.driver.find_element_by_link_text("Request a Record").click()
            time.sleep(1)

            form = self.driver.find_element_by_id("submit")
            time.sleep(1)
            form.submit()

            self.assertTrue(self.driver.find_element_by_id("parsley-id-7"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-9"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-11"))

            select = Select(self.driver.find_element_by_id("request-category"))
            select.select_by_value("Culture & Recreation")
            time.sleep(1)

            select = Select(self.driver.find_element_by_id("request-agency"))
            select.select_by_value("0860")
            time.sleep(1)

            self.driver.find_element_by_id("request-title").send_keys(
                "A request title can only be 90 characters in length. A request title can only be 90 charac100")
            time.sleep(1)

            self.assertTrue(self.driver.find_element_by_id("title-character-count"))

            self.driver.find_element_by_id("request-title").clear()
            self.driver.find_element_by_id("request-title").send_keys("TEST REQUEST TITLE")
            time.sleep(1)

            #self.driver.find_element_by_id("request-description").send_keys(
            #    "This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is100")
            #time.sleep(1)

            self.assertTrue(self.driver.find_element_by_id("description-character-count"))

            self.driver.find_element_by_id("request-description").clear()
            self.driver.find_element_by_id("request-description").send_keys("TEST REQUEST DESCRIPTION")
            time.sleep(1)

            self.driver.find_element_by_id("request-file").send_keys(
                "C:\\Users\\bwaite\\Desktop\\Test_files\\Test1.docx")
            time.sleep(1)

            form = self.driver.find_element_by_id("submit")
            time.sleep(1)
            form.submit()

            self.assertTrue(self.driver.find_element_by_class_name("alert-success"))

        else:
            self.driver.find_element_by_link_text("Request a Record").click()
            time.sleep(1)

            form = self.driver.find_element_by_id("submit")
            time.sleep(1)
            form.submit()

            self.assertTrue(self.driver.find_element_by_id("parsley-id-7"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-9"))
            self.assertTrue(self.driver.find_element_by_id("parsley-id-11"))

            select = Select(self.driver.find_element_by_id("request-category"))
            select.select_by_value("Culture & Recreation")
            time.sleep(1)

            select = Select(self.driver.find_element_by_id("request-agency"))
            select.select_by_value("0860")
            time.sleep(1)

            #self.driver.find_element_by_id("request-title").send_keys(
            #    "A request title can only be 90 characters in length. A request title can only be 90 charac100")
            #time.sleep(1)

            self.assertTrue(self.driver.find_element_by_id("title-character-count"))

            self.driver.find_element_by_id("request-title").clear()
            self.driver.find_element_by_id("request-title").send_keys("TEST REQUEST TITLE")
            time.sleep(1)

            # self.driver.find_element_by_id("request-description").send_keys(
            #    "This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is100")
            # time.sleep(1)

            self.assertTrue(self.driver.find_element_by_id("description-character-count"))

            self.driver.find_element_by_id("request-description").clear()
            self.driver.find_element_by_id("request-description").send_keys("TEST REQUEST DESCRIPTION")
            time.sleep(1)

            self.driver.find_element_by_id("request-file").send_keys(
                "C:\\Users\\bwaite\\Desktop\\Test_files\\Test1.docx")
            time.sleep(1)

            self.driver.find_element_by_id("first-name").send_keys("John")
            time.sleep(1)

            self.driver.find_element_by_id("last-name").send_keys("Doris")
            time.sleep(1)

            self.driver.find_element_by_id("email").send_keys("john.doris0860@gmail.com")
            time.sleep(1)

            self.driver.find_element_by_id("user-title").send_keys("User's Title")
            time.sleep(1)

            self.driver.find_element_by_id("user-organization").send_keys("User's Organization")
            time.sleep(1)

            self.driver.find_element_by_id("phone").send_keys("5555555555")
            time.sleep(1)

            self.driver.find_element_by_id("fax").send_keys("5555555555")
            time.sleep(1)

            self.driver.find_element_by_id("address-line-1").send_keys("123 Main Street")
            time.sleep(1)

            self.driver.find_element_by_id("address_two").send_keys("Apt 3D")
            time.sleep(1)

            self.driver.find_element_by_id("city").send_keys("New York")
            time.sleep(1)

            self.driver.find_element_by_id("zipcode").send_keys("12345")
            time.sleep(1)

            form = self.driver.find_element_by_name("submit")
            form.submit()
            time.sleep(1)

            self.assertTrue(self.driver.find_element_by_class_name("alert-success"))



