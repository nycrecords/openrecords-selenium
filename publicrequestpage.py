from selenium.webdriver.support.ui import Select
import time


class RequestPage:
    def __init__(self, driver):
        self.driver = driver

    def agency_request(self):

        self.driver.find_element_by_link_text("Request a Record").click()
        time.sleep(.25)

        form = self.driver.find_element_by_id("submit")
        time.sleep(.25)
        form.submit()

        if self.driver.find_element_by_id("parsley-id-7"):
            print ("Agency dropdown error: 'This value is required' - checked")
        else:
            print ("Missing error message for Agency dropdown")

        if self.driver.find_element_by_id("parsley-id-9"):
            print ("Request Title error: 'This value is required' - checked")
        else:
            print ("Missing error message for Request Title empty")

        if self.driver.find_element_by_id("parsley-id-11"):
            print ("Request Description error: 'This value is required' - checked")
        else:
            print ("Missing error message for Request Description empty")

        select = Select(self.driver.find_element_by_id("request-category"))
        select.select_by_value("Culture & Recreation")
        time.sleep(.25)

        select = Select(self.driver.find_element_by_id("request-agency"))
        select.select_by_value("0860")
        time.sleep(.25)

        self.driver.find_element_by_id("request-title").send_keys("A request title can only be 90 characters in length. A request title can only be 90 charac100")
        time.sleep(.25)

        if self.driver.find_element_by_id("title-character-count"):
            print("Max character limit is 90")
        else:
            print("Missing error message for Request Title greater than 90")

        self.driver.find_element_by_id("request-title").clear()
        self.driver.find_element_by_id("request-title").send_keys("TEST REQUEST TITLE")
        time.sleep(.25)

        self.driver.find_element_by_id("request-description").send_keys("This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is a test comment. This is100")
        time.sleep(.25)

        if self.driver.find_element_by_id("description-character-count"):
            print("Max character limit is 5000")
        else:
            print("Missing error message for Request Description greater than 5000")

        self.driver.find_element_by_id("request-description").clear()
        self.driver.find_element_by_id("request-description").send_keys("TEST REQUEST DESCRIPTION")
        time.sleep(.25)

        self.driver.find_element_by_id("request-file").send_keys("C:\\Users\\bwaite\\Desktop\\Test_files\\Test1.docx")
        time.sleep(.25)

        form = self.driver.find_element_by_id("submit")
        time.sleep(.25)
        form.submit()

        if self.driver.find_element_by_id("session-warning-modal"):
            print ("Request submitted successfully")
        else:
            print ("Request was not submitted")
