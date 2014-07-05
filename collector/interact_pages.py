import mechanize
from selenium import webdriver


def driver_factory(use_selenium=False, driver='Firefox', **params):
    if use_selenium:
        return _Selenium(driver=driver, **params)
    else:
        return _Mechanize(**params)


class _Selenium(object):

    def __init__(self, driver='Firefox', **params):
        self.driver = driver
        self.params = params
    @property
    def browser(self):
        driver = None
        if self.driver.lower() == 'firefox':
            driver = webdriver.Firefox(**self.params)
        elif self.driver.lower() == 'phantomjs':
            driver = webdriver.PhantomJS(**self.params)
        return driver

    def open(self, url, **kw):
        browser = self.browser
        return browser.get(url)


# actually the only part that is really plumbed into the
# the harvest script it the selenium
class _Mechanize(object):

    def __init(self, **params):
        self.params = params

    @property
    def browser(self):
        return mechanize.Browser()

    def open(self, url, **kw):
        return self.browser.open(url, **kw)

