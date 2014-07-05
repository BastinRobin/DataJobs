import BeautifulSoup
from lxml import html


class Page(object):

    def __init__(self, page_source):
        self.source = page_source
        self.soup = BeautifulSoup.BeautifulSoup(page_source)
        self.html = html.fromstring(page_source)

    def xpath(self, xpath):
        return self.html.xpath(xpath)
