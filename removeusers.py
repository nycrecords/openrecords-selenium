from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest
import time

#this class will take find the request with the nearest due date, fill it up with junk data and then close it

class FixUsers(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def users(self, user_type):
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
            self.driver.find_element_by_link_text("Add User").click()
            time.sleep(.5)
            selectuser = Select(self.driver.find_element_by_id('user'))
            self.driver.find_element_by_id('user').click()
            selectuser.select_by_visible_text('Test Three (TestThree@records.nyc.gov)')
            time.sleep(.25)
            selectpreset = Select(self.driver.find_element_by_id('role'))
            selectpreset.select_by_visible_text('Agency Helper')
            time.sleep(.25)
            selectperms = Select(self.driver.find_element_by_id('permission'))
            selectperms.select_by_visible_text('Close Request')
            time.sleep(.25)
            self.driver.find_element_by_xpath('//*[@id="add_options"]/button').click()
            time.sleep(.25)
            self.driver.find_element_by_xpath('//*[@id="add-user-request"]/div/fieldset/div[2]/button[2]').click()
            time.sleep(.25)

        except NoSuchElementException:
            pass

        self.driver.find_element_by_link_text("Edit User").click()
        time.sleep(.25)
        selectedituser = Select(self.driver.find_element_by_xpath('(//*[@id="user"])[2]'))
        time.sleep(.25)
        self.driver.find_element_by_xpath('(//*[@id="user"])[2]').click()
        time.sleep(.25)
        selectedituser.select_by_value('4013968AF214A5436AB34013968AF214')
        time.sleep(.25)
        selectrole= Select(self.driver.find_element_by_xpath('(//*[@id="role"])[2]'))
        selectrole.select_by_value('4')
        time.sleep(.25)
        selectrole.select_by_value('2')
        time.sleep(.25)
        selecteditperms = Select(self.driver.find_element_by_xpath('(//*[@id="permission"])[2]'))
        time.sleep(.25)
        selecteditperms.select_by_visible_text('Close Request')
        time.sleep(.25)
        self.driver.find_element_by_xpath('//*[@id="edit_options"]/button').click()
        time.sleep(.5)
        try:
            self.driver.find_element_by_xpath('//*[@id="edit-user-request"]/div/fieldset/div[2]/button[2]').click()
        except ElementNotVisibleException:
            selectrole= Select(self.driver.find_element_by_xpath('(//*[@id="role"])[2]'))
            selectrole.select_by_value('4')
            time.sleep(.25)
            selecteditperms = Select(self.driver.find_element_by_xpath('(//*[@id="permission"])[2]'))
            time.sleep(.25)
            selecteditperms.select_by_visible_text('Close Request')
            time.sleep(.25)
            self.driver.find_element_by_xpath('//*[@id="edit_options"]/button').click()



        self.driver.find_element_by_link_text("Remove User").click()
        time.sleep(2)
        selectremove = Select(self.driver.find_element_by_xpath('(//*[@id="user"])[3]'))
        selectremove.select_by_value('4013968AF214A5436AB34013968AF214')
        print('select found')
        self.driver.find_element_by_xpath('//*[@id="remove-user-request"]/div/fieldset/div[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="remove-user-request"]/div/fieldset/div[2]/div/input').send_keys('REMOVE')
        time.sleep(.25)
        self.driver.find_element_by_xpath('//*[@id="remove-user-request"]/div/fieldset/div[2]/button[2]').click()