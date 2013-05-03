from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BROWSER = 'Firefox'

class OpenPage(object):

    def __init__(self, browser=BROWSER, **kw):
        self.Keys = Keys
        self.browser = browser

        for k, v in kw.items(): setattr(self, k, v)

    def set_driver(self):
        # todo: add more browsers
        self.driver = webdriver.Firefox()

    def open_page(self, url):
        self.driver.get(url)

    def find_xpath(self, xpaths):
        paths = self.driver.find_element_by_xpath(xpaths)
        return paths

    def click_element(self, element):
        return element.click()

    def send(self, element, text):
        return element.send_keys(text)

    @property
    def open(self):
        self.driver.open()

    @property
    def source(self):
        return self.driver.page_source

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def close(self):
        self.driver.quit()

