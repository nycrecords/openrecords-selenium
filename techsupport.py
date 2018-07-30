from selenium import webdriver
import unittest
import time

class TechSupport(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def techsupport(self, user_type):
        self.driver.find_element_by_link_text("Technical Support").click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Firstname Lastname')
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('fakeemail@fake.com')
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys("TEST")
        self.driver.find_element_by_xpath('//*[@id="message"]').send_keys('TEST MESSAGETEST MESSAGETEST MESSAGETEST MESSAGETEST MESSAGETEST MESSAGETEST MESSAGE')
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
