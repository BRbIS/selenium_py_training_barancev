__author__ = 'agorgoma'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        myProxy = "http://172.17.8.10:8080"

        proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy':''})

        self.driver = webdriver.Remote(
            command_executor='http://192.168.1.8:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX(proxy=proxy))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()