__author__ = 'agorgoma'

from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import driver

base_url = "http://172.17.10.17/"

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def login(driver):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()

def test_login(driver):
    driver.get(base_url + "/php4dvd/")
    login(driver)
    logout(driver)
