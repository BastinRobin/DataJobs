from nose.tools import ok_
from nose.tools import raises
from urllib2 import URLError
from collector.collect_pages import GetPage, Page

URL = 'http://www.google.com'

def test_collector_get_page():
    GetPage()

def test_collector_get_page_url():
    url = GetPage.open(URL)
    ok_(url.code == 200)
    ok_(url.msg == 'OK')

def test_collector_page():
    Page(URL)

@raises(URLError)
def test_collector_get_page_raises_URLError():
    url = GetPage.open(URL + '11111')

