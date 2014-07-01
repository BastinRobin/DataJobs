import urllib2

class GetPage(object):

    def __init__(self, **kw):
        for k, v in kw.items(): setattr(self, k, v)

    def urlopen(self, url):
        return urllib2.urlopen(url)

    @classmethod
    def open(cls, url):
        cls = cls()
        page = cls.urlopen(url)
        if page.code != 200:
            raise UnexpectedHtmlReturnCode('Page "{}" returned "{}"'.format(url, page.code))
        return page


class ReadPage(object):

    def __init__(self, url):
        self.page = GetPage.open(url)
        self.source = self.page.read()


class UnexpectedHtmlReturnCode(Exception):
    pass
