# coding=utf-8
__author__ = 'agorgoma'

from model.application import Application
from selenium import webdriver
import pytest

# base_url = "http://172.17.10.17/"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser type")
    parser.addoption("--base_url", action="store", default="http://172.17.10.17/php4dvd/", help="base URL")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


# TODO придумать что-то с сылками на сервер для дома и офиса
@pytest.fixture(scope="session")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.FIREFOX)
    # FIXME разобраться у удаленным запуском хрома(сервер пишет нужно указать какие-то опции)
    elif browser_type == "chrome":
        driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.CHROME)
    # TODO установить драйвер для IE
    elif browser_type == "ie":
        driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.Ie)
    # driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)