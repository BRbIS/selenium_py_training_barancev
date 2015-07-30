# coding=utf-8
__author__ = 'agorgoma'

from model.application import Application
from selenium import webdriver
import pytest


# TODO придумать что-то с сылками на сервер для дома и офиса

@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.FIREFOX)
    elif browser_type == "chrome":
        driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.CHROME)
    # TODO установить драйвер для IE
    elif browser_type == "ie":
        driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.Ie)
    # driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)
