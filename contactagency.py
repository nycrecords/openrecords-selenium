from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest
import time



class ContactAgency(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def contact(self, user_type):
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

        self.driver.find_element_by_id('MainNavHelp').click()
        time.sleep(.5)

        self.driver.find_element_by_id('first-name').send_keys("Yes")
        self.driver.find_element_by_id('last-name').send_keys('Man')
        self.driver.find_element_by_id('email').send_keys('yesman@no.com')
        self.driver.find_element_by_id('message').send_keys("HELLO THIS A MESSAGE YES")
        time.sleep(.25)
        self.driver.find_element_by_id('submit').click()
        time.sleep(.25)
        

