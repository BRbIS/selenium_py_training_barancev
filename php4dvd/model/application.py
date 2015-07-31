__author__ = 'agorgoma'

#base_url = "http://172.17.10.17/"

from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class Application(object):

    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.login_page = LoginPage(driver, base_url)
        self.wait = WebDriverWait(driver, 10)
        self.internal_page = InternalPage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def is_logged_in(self):
        return self.login_page.is_this_page

    def is_not_logged_in(self):
        return self.internal_page.is_this_page
