import urllib2
import httplib2
from urllib import urlencode
from logging import debug, info


class GetPage(object):

    def __init__(self, **kw):
        for k, v in kw.items(): setattr(self, k, v)


    def urlopen(self, url):
        return urllib2.urlopen(url)

    @classmethod
    def open(cls, url):
        cls = cls()
        return cls.urlopen(url)

class GetDataFromForms(object):

    def __init__(self, page_url, data, action='POST', timeout=10):
        self.url = page_url
        self.data = urlencode(data)
        self.action = action
        self.http = httplib2.Http(timeout=timeout)

    def request_form(self):
        debug(self.data)
        resp, content = self.http.request(
            self.url,
            self.action,
            self.data
        )
        return resp, content

    @classmethod
    def request(cls, url, data):
        cls = cls(url, data)
        resp, cont = cls.request_form()
        if not int(resp['status']) == 200:
            raise Exception("Unable to open: %s", url)
        return cont
