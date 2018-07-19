from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest
import time

#this class will take find the request with the nearest due date, fill it up with junk data and then close it

class HandleRequest(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def handle_request(self, user_type):
        self.driver.find_element_by_link_text("Search Requests").click()
        time.sleep(.5)

        if user_type == "public" or user_type == "anonymous":
            self.driver.find_element_by_id("advanced-options-toggle").click()
            self.driver.find_element_by_name("closed").click()
            selecttype = Select(self.driver.find_element_by_id("agency_ein"))
            selecttype.select_by_value("0860")
            self.driver.find_element_by_id("query").send_keys("test")
            time.sleep(.25)

            self.driver.find_element_by_id("search").click()
            time.sleep(.25)

            self.driver.find_element_by_id("sort_date_due").click()
            time.sleep(.25)

            self.driver.find_element_by_xpath('//*[@id="results"]/a[1]').click()
            time.sleep(.25)

        if user_type == "user":
            selecttype = Select(self.driver.find_element_by_id("agency_ein"))
            selecttype.select_by_value("0860")
            self.driver.find_element_by_id("query").send_keys("test")
            time.sleep(.25)

            self.driver.find_element_by_id("search").click()
            time.sleep(.25)

            self.driver.find_element_by_id("sort_date_due").click()
            time.sleep(.25)

            self.driver.find_element_by_xpath('//*[@id="results"]/a[1]').click()
            time.sleep(.25)

        if user_type == "admin":
            selecttype = Select(self.driver.find_element_by_id("agency_ein"))
            selecttype.select_by_value("0860")
            self.driver.find_element_by_id("query").send_keys("test")
            time.sleep(.25)

            self.driver.find_element_by_id("search").click()
            time.sleep(.25)

            self.driver.find_element_by_id("sort_date_due").click()
            time.sleep(.25)

            self.driver.find_element_by_xpath('//*[@id="results"]/a[1]').click()
            time.sleep(.25)

            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div/div[4]/div[2]/label[1]').click()
            self.driver.find_element_by_xpath('//*[@id="agency_request_summary"]').click()
            self.driver.find_element_by_xpath('//*[@id="agency-request-summary"]').send_keys('20 characters are needed to finish this test')
            self.driver.find_element_by_xpath('//*[@id="agency-request-summary"]').send_keys(Keys.ENTER)
            time.sleep(.25)

            try:
                if self.driver.find_element_by_link_text("Acknowledge").is_displayed:
                    self.driver.find_element_by_link_text("Acknowledge").click()
                    time.sleep(.25)

                    selectdays = Select(self.driver.find_element_by_id("acknowledgment-email-days"))
                    selectdays.select_by_value("90")
                    time.sleep(.25)
                    
                    self.driver.find_element_by_id("acknowledgment-email-info-text").clear()
                    self.driver.find_element_by_id("acknowledgment-email-info-text").send_keys("This is a test response")
                    time.sleep(.25)

                    self.driver.find_element_by_xpath('//*[@id="add-acknowledgment"]/div/fieldset/div[2]/button[2]').click()
                    time.sleep(.25)

                    self.driver.find_element_by_xpath('//*[@id="add-acknowledgment"]/div/fieldset/div[3]/button[2]').click()
                    time.sleep(.25)

                    self.driver.find_element_by_xpath('//*[@id="add-acknowledgment"]/div/fieldset/div[4]/button[2]').click()
                    time.sleep(.25)
                else:
                    pass
            except NoSuchElementException:
                pass

                
            
            self.driver.find_element_by_link_text("Add File").click()
            self.driver.find_element_by_id("add-files").send_keys('/Users/bzhuang/Documents/testFiles')

            self.driver.find_element_by_xpath('//*[@id="mobile-toggle"]/ul/li[2]/a').click()
            self.driver.find_element_by_id("link-title").send_keys("Test link")
            self.driver.find_element_by_id("link-url").send_keys("https://openrecords-test.appdev.records.nycnet/")
            self.driver.find_elements_by_xpath("//input[@name='privacy' and @value='release_public']")
            time.sleep(.25)
            self.driver.find_element_by_id("link-next-1").click()
            time.sleep(.25)
            self.driver.find_element_by_id("link-next-2").click()
            time.sleep(.25)
            self.driver.find_element_by_id("link-submit").click()
            time.sleep(.25)

            self.driver.find_element_by_link_text("Add Instructions").click()
            self.driver.find_element_by_id("instruction-content").clear()
            self.driver.find_element_by_id("instruction-content").send_keys("No further instructions test")
            self.driver.find_element_by_xpath('//*[@id="instruction-first"]/div[1]/label/input')
            self.driver.find_element_by_id("instruction-next-1").click()
            time.sleep(.25)
            self.driver.find_element_by_id("instruction-next-2").click()
            time.sleep(.25)
            self.driver.find_element_by_id("instruction-submit").click()
            time.sleep(.25)

            self.driver.find_element_by_link_text("Add Note").click()
            self.driver.find_element_by_id("note-content").clear()
            self.driver.find_element_by_id("note-content").send_keys("No further notes test")
            self.driver.find_element_by_xpath('//*[@id="note-first"]/div[1]/label/input')
            self.driver.find_element_by_id("note-next-1").click()
            time.sleep(.25)
            self.driver.find_element_by_id("note-next-2").click()
            time.sleep(.25)
            self.driver.find_element_by_id("note-submit").click()
            time.sleep(.25)

            self.driver.find_element_by_link_text("Extend").click()
            selectextend = Select(self.driver.find_element_by_id('extension-select'))
            selectextend.select_by_index(2)
            print("HERE3")
            self.driver.find_element_by_id("extension-reason").send_keys("YES123456789123455678")
            print("HERE4")
            self.driver.find_element_by_id("extension-next-2").click()
            self.driver.find_element_by_id("extension-next-3").click()
            self.driver.find_element_by_id("extension-submit").click()
            time.sleep(.25)

            self.driver.find_element_by_link_text("Close").click()
            selectclosing = Select(self.driver.find_element_by_id("closing-reason-ids"))
            selectclosing.select_by_visible_text("Fulfilled in Whole")
            selectclosing.select_by_value("3")
            self.driver.find_element_by_xpath('//*[@id="add-closing"]/div/fieldset/div[2]/button[2]').click()
            time.sleep(.25)

            self.driver.find_element_by_xpath('//*[@id="add-closing"]/div/fieldset/div[3]/button[2]').click()
            time.sleep(.25)

            self.driver.find_element_by_xpath('//*[@id="add-closing"]/div/fieldset/div[4]/button[2]').click()
            time.sleep(4)


