__author__ = 'agorgoma'

# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class CreateMovie(unittest.TestCase):
    # Connect to remote server
    def setUp(self):
        self.driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.17.10.17/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_movie(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("11111")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Title")
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("Also known as")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("1898")
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("60")
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys("10")
        driver.find_element_by_id("submit").click()

#TODO check new movie after create and in list on home page

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
'''
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
'''
if __name__ == "__main__":
    unittest.main()