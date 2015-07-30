__author__ = 'agorgoma'

from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app

''' \\move to application
base_url = "http://172.17.10.17/"


def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()


def login(driver, user):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(user.password)
    driver.find_element_by_name("submit").click()
'''


def test_login_with_invalid_credentials(app):
    app.go_to_home_page()
    app.login(User.random())
    assert app.is_not_logged_in()


def test_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()

