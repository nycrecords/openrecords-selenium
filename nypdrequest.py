from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import unittest


class nypdrequest(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def nypdrequestfun(self, user_type):


        agency = "0056"
        title= 'test'
        description = 'test description'

        foilfeilds = {'FOIL':'',
        'Agency':agency, 
        'Title':title,
        'Description':description        
        }

        self.driver.find_element_by_link_text("Request a Record").click()
        time.sleep(.25)

        form = self.driver.find_element_by_id("submit")
        time.sleep(.25)
        form.submit()    

        select = Select(self.driver.find_element_by_id("request-agency"))
        select.select_by_value(agency)
        time.sleep(.25)

        self.driver.find_element_by_id("request-title").clear()
        self.driver.find_element_by_id("request-title").send_keys(title)
        time.sleep(.25)

        #self.driver.assertTrue("hey",self.driver.find_element_by_id("description-character-count").is_displayed())

        self.driver.find_element_by_id("request-description").clear()
        self.driver.find_element_by_id("request-description").send_keys(description)
        time.sleep(.25)

        selecttype = Select(self.driver.find_element_by_id("request-type-1"))
        selecttype.select_by_value("1")
        time.sleep(.25)

        self.driver.find_element_by_id("arrest-report-number-1").clear()
        self.driver.find_element_by_id("arrest-report-number-1").send_keys("1234")
        time.sleep(.25)

        self.driver.find_element_by_id("precinct-number-1").clear()
        self.driver.find_element_by_id("precinct-number-1").send_keys("1234")
        time.sleep(.25)

        self.driver.find_element_by_id("arrest-report-name-1").clear()
        self.driver.find_element_by_id("arrest-report-name-1").send_keys("OFFICER COOL GUY")
        time.sleep(.25)

        self.driver.find_element_by_id("arrest-report-date-1").clear()
        self.driver.find_element_by_id("arrest-report-date-1").send_keys("05/05/2018")
        time.sleep(.25)

        self.driver.find_element_by_id("arrest-report-dob-1").clear()
        self.driver.find_element_by_id("arrest-report-dob-1").send_keys("05/05/1937")
        time.sleep(.25)

        self.driver.find_element_by_id("arrest-report-victim-complainant-name-1").clear()
        self.driver.find_element_by_id("arrest-report-victim-complainant-name-1").send_keys("me irl")
        time.sleep(.25)

        self.driver.find_element_by_id("arrest-report-charge-1").clear()
        self.driver.find_element_by_id("arrest-report-charge-1").send_keys("test")
        time.sleep(.25)

        # self.driver.find_element_by_id("custom-request-form-additional-content").click()
        # time.sleep(.25)

        # selecttype2 = Select(self.driver.find_element_by_id("request-type-2"))
        # selecttype2.select_by_value("1")
        # time.sleep(.25)

        # self.driver.find_element_by_id("arrest-report-number-2").clear()
        # self.driver.find_element_by_id("arrest-report-number-2").send_keys("1234")
        # time.sleep(.25)

        # self.driver.find_element_by_id("precinct-number-2").clear()
        # self.driver.find_element_by_id("precinct-number-2").send_keys("1234")
        # time.sleep(.25)


        # self.driver.find_element_by_id("arrest-report-name-2").clear()
        # self.driver.find_element_by_id("arrest-report-name-2").send_keys("OFFICER COOL GUY")
        # time.sleep(.25)

        # self.driver.find_element_by_id("arrest-report-date-2").clear()
        # self.driver.find_element_by_id("arrest-report-date-2").send_keys("05/05/2018")
        # time.sleep(.25)


        # self.driver.find_element_by_id("arrest-report-dob-2").clear()
        # self.driver.find_element_by_id("arrest-report-dob-2").send_keys("05/05/1937")
        # time.sleep(.25)

        # self.driver.find_element_by_id("arrest-report-victim-complainant-name-2").clear()
        # self.driver.find_element_by_id("arrest-report-victim-complainant-name-2").send_keys("me irl")
        # time.sleep(.25)

        # self.driver.find_element_by_id("arrest-report-charge-2").clear()
        # self.driver.find_element_by_id("arrest-report-charge-2").send_keys("test")
        # time.sleep(.25)

        # self.driver.find_element_by_id("custom-request-form-additional-content").click()
        # time.sleep(.25)

        # selecttype3 = Select(self.driver.find_element_by_id("request-type-3"))
        # selecttype3.select_by_value("2")
        # time.sleep(.25)
            
        # self.driver.find_element_by_id("complaint-report-number-1").clear()
        # self.driver.find_element_by_id("complaint-report-number-1").send_keys("test")
        # time.sleep(.25)

        # self.driver.find_element_by_id("precinct-number-1").clear()
        # self.driver.find_element_by_id("precinct-number-1").send_keys("12312")
        # time.sleep(.25)

        # self.driver.find_element_by_id("complaint-report-date-1").clear()
        # self.driver.find_element_by_id("complaint-report-date-1").send_keys("05/23/32")
        # time.sleep(.25)

        # self.driver.find_element_by_id("complaint-report-time-1").send_keys("400")
        # time.sleep(.25)

        # self.driver.find_element_by_id("complaint-report-address-1").clear()
        # self.driver.find_element_by_id("complaint-report-address-1").send_keys("123 This Street Street")
        # time.sleep(.25)

        # self.driver.find_element_by_id("victim-complainant-name-1").clear()
        # self.driver.find_element_by_id("victim-complainant-name-1").send_keys("TESTNAME")
        # time.sleep(.25)

        # self.driver.find_element_by_id("complaint-report-offense-1").clear()
        # self.driver.find_element_by_id("complaint-report-offense-1").send_keys("existing")
        # time.sleep(.25)

        # self.driver.find_element_by_id("custom-request-form-additional-content").click()
        # time.sleep(.25)

        # selecttype4 = Select(self.driver.find_element_by_id("request-type-4"))
        # selecttype4.select_by_value("3")
        # time.sleep(.25)

        # self.driver.find_element_by_id("date-of-incident-1").clear()
        # self.driver.find_element_by_id("date-of-incident-1").send_keys("05/05/05")
        # time.sleep(.25)

        # self.driver.find_element_by_id("start-time-1").send_keys("300")
        # self.driver.find_element_by_id("end-time-1").send_keys("400")
        # time.sleep(.25)

        # self.driver.find_element_by_id("bwc-location-1").clear()
        # self.driver.find_element_by_id("bwc-location-1").send_keys("brooklyn")
        # time.sleep(.25)

        # self.driver.find_element_by_id("precinct-number-1").clear()
        # self.driver.find_element_by_id("precinct-number-1").send_keys("141244211241241")

        # self.driver.find_element_by_id("type-of-incident-1").clear()
        # self.driver.find_element_by_id("type-of-incident-1").send_keys("SUPER DUPER TEST")
        # time.sleep(.25)

        # self.driver.find_element_by_id("officers-name-1").clear()
        # self.driver.find_element_by_id("officers-name-1").send_keys("super cool officer")
        # time.sleep(.25)

        # self.driver.find_element_by_id("arrest-number-1").clear()
        # self.driver.find_element_by_id("arrest-number-1").send_keys("2")
        # time.sleep(.25)

        # self.driver.find_element_by_id("complaint-number-1").clear()
        # self.driver.find_element_by_id("complaint-number-1").send_keys("1")
        # time.sleep(.25)

        # self.driver.find_element_by_id("other-police-incident-number-1").clear()
        # self.driver.find_element_by_id("other-police-incident-number-1").send_keys("10")
        # time.sleep(.25)

        if user_type == 'anonymous':
            self.driver.find_element_by_id("first-name").clear()
            self.driver.find_element_by_id("first-name").send_keys("Whomst")
            time.sleep(.25)

            self.driver.find_element_by_id("last-name").clear()
            self.driver.find_element_by_id("last-name").send_keys("t've")
            time.sleep(.25)

            self.driver.find_element_by_id("email").send_keys("john.doris0860@gmail.com")
            time.sleep(.25)

            self.driver.find_element_by_id("user-title").send_keys("User's Title")
            time.sleep(.25)

            self.driver.find_element_by_id("user-organization").send_keys("User's Organization")
            time.sleep(.25)

            self.driver.find_element_by_id("phone").send_keys("5555555555")
            time.sleep(.25)

            self.driver.find_element_by_id("fax").send_keys("5555555555")
            time.sleep(.25)

            self.driver.find_element_by_id("address-line-1").send_keys("123 Main Street")
            time.sleep(.25)

            self.driver.find_element_by_id("address_two").send_keys("Apt 3D")
            time.sleep(.25)

            self.driver.find_element_by_id("city").send_keys("New York")
            time.sleep(.25)

            self.driver.find_element_by_id("zipcode").send_keys("12345")
            time.sleep(.25)

        form = self.driver.find_element_by_name("submit")
        form.submit()
        time.sleep(.25) 

        
        
        foilid = self.driver.find_element_by_id("request-id").text

        
        
        
        foilfeilds['FOIL'] = foilid
        print(foilfeilds['FOIL'])
        self.assertTrue("The success message did not show up" , self.driver.find_element_by_class_name("alert-success"))
        return foilfeilds