import unittest
from splinter.driver import WebDriver
from ludibrio import Mock, Stub


class WebDriverTest(unittest.TestCase):
    "WebDriver"

    def test_visit(self):
        "WebDriver.visit should call browser.get"

        with Mock() as firefox_mock:
            firefox_mock.get('http://foo.com')

        with ReplaceBrowser(firefox_mock):
            driver = WebDriver()
            driver.visit('http://foo.com')

        firefox_mock.validate()

    def test_title(self):
        "WebDriver.title should call browser.title"

        with Mock() as firefox_mock:
            firefox_mock.get_title()

        with ReplaceBrowser(firefox_mock):
            driver = WebDriver()
            driver.title

        firefox_mock.validate()

    def test_quit(self):
        "WebDriver.quit should call browser.quit"

        with Mock() as firefox_mock:
            firefox_mock.quit()

        with ReplaceBrowser(firefox_mock):
            driver = WebDriver()
            driver.quit()

        firefox_mock.validate()


class ReplaceBrowser(object):

    def __init__(self, driver_mock):
        with Stub() as browser:
            from selenium.firefox.webdriver import WebDriver as browser
            browser() >> driver_mock
        self.browser = browser

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        self.browser.restore_import()


