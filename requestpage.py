from selenium.webdriver.support.ui import Select
from searchtest import SearchTest
from selenium.webdriver.common.keys import Keys
import time


            self.driver.find_element_by_id("title").click()
            time.sleep(1)
            self.driver.find_element_by_id("request-title").clear()
            time.sleep(1)
            self.driver.find_element_by_id("request-title").send_keys("TEST REQUEST TITLE - EDIT")
            time.sleep(1)
            self.driver.find_element_by_id("submitBtn").click()
            time.sleep(1)

            #clicks Title but not agency request summary... same class name.. does not click back to Public
            self.driver.find_element_by_class_name("btn-group").click()
            time.sleep(2)
            self.driver.find_element_by_class_name("title-privacy-btn").click()

            self.driver.find_element_by_id("agency_request_summary").click()
            self.driver.find_element_by_id("agency-request-summary").clear()
            self.driver.find_element_by_id("agency-request-summary").send_keys("AGENCY REQUEST SUMMARY")
            self.driver.find_element_by_id("submitBtn").click()

            self.driver.find_element_by_class_name("desc-privacy-btn").click()
            time.sleep(2)
            self.driver.find_element_by_class_name("btn-group").click()

            #priv_but = self.driver.find_element_by_class_name("title-privacy-btn")

            time.sleep(3)