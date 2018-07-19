from searchtest import SearchTest
from selenium.webdriver.common.keys import Keys
import time
import nypdrequest

# date submitted, date due, date closed variable
date_from = "10/19/2017"
date_to = "10/31/2017"

# FOIL ID variables
s_foil_id = "FOIL-2018-860-00001"
s_title = "FOIL-2018-860-00003"
s_desc = "FOIL-2018-860-00003"
s_agency_sum = "FOIL-2018-860-00004"
s_requester = "FOIL-2018-860-00005"
s_sub = "FOIL-2018-860-00001"
s_due = "FOIL-2018-860-00002"
s_closed = "FOIL-2018-860-00009"


"""
requestinfo is a python dictionary in the format

{'FOIL':'',
'Agency':agency, 
'Title':title,
'Description':description}

from nypdrequestfun where the information is the information that created the request
"""


requestinfo = ''

class RequestPage(SearchTest):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        requestinfo = nypdrequest.nypdrequest(self.driver).nypdrequestfun(self.user_type)

    # search by FOIL ID
    def search_foil_id(self, user_type):
        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_name("foil_id").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys(requestinfo['FOIL'])
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(requestinfo['FOIL']).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)
        else:
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys(requestinfo['FOIL'])
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(requestinfo['FOIL']).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_id("advanced-options-toggle").click()
            time.sleep(.25)
            self.driver.find_element_by_name("foil_id").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys(requestinfo['FOIL'])
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(requestinfo['FOIL']).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)

    # search by Title
    def search_title(self, user_type):

        requestinfo = nypdrequest.nypdrequest(self.driver).nypdrequestfun(self.user_type)


        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys(requestinfo['Title'])
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(s_title).click()
            time.sleep(.25)
        else:
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys(requestinfo['Title'])
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(requestinfo['Title']).click()
            time.sleep(.25)

    #search by Description
    def search_description(self, user_type):

        requestinfo = nypdrequest.nypdrequest(self.driver).nypdrequestfun(self.user_type)


        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_name("title").click()
            time.sleep(.25)
            self.driver.find_element_by_name("description").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys(requestinfo['Description'])
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(requestinfo['Description']).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)

    # search by Agency Request Summary
    def search_agency_request_summary(self, user_type):
        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_name("title").click()
            time.sleep(.25)
            self.driver.find_element_by_name("agency_request_summary").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys("blueberry")
            time.sleep(.25)
            self.driver.find_element_by_name("closed").click()
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(s_agency_sum).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)

    # search by Requester Name
    def search_requester_name(self, user_type):
        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_name("title").click()
            time.sleep(.25)
            self.driver.find_element_by_name("requester_name").click()
            time.sleep(.25)
            self.driver.find_element_by_id("query").send_keys("blueberry")
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(s_requester).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)

    # search Date Submitted
    def search_date_submitted(self, user_type):
        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_id("date-rec-from").send_keys(date_from)
            time.sleep(.25)
            self.driver.find_element_by_id("date-rec-to").send_keys(date_to)
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,600)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(s_sub).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)

    # search Due Date
    def search_due_date(self, user_type):
        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_id("date-due-from").send_keys(date_from)
            time.sleep(.25)
            self.driver.find_element_by_id("date-due-to").send_keys(date_to)
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(s_due).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)

    # search Closed Date
    def search_closed_date(self, user_type):
        if user_type == "admin" or user_type == "user":
            self.driver.find_element_by_link_text("Search Requests").click()
            time.sleep(.25)
            self.driver.find_element_by_name("closed").click()
            time.sleep(.25)
            self.driver.find_element_by_id("date-closed-from").send_keys(date_from)
            time.sleep(.25)
            self.driver.find_element_by_id("date-closed-to").send_keys(date_to)
            time.sleep(.25)
            self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
            time.sleep(.25)
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(.25)
            self.driver.find_element_by_partial_link_text(s_closed).click()
            time.sleep(.25)
            self.assertTrue(self.driver.find_element_by_class_name("request-label"))
            time.sleep(.25)