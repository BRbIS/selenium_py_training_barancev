__author__ = 'agorgoma'

from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Remote('http://172.17.10.17:4444/wd/hub', webdriver.DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver