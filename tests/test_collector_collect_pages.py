from nose.tools import ok_
from nose.tools import raises
from urllib2 import URLError
from collector.collect_pages import GetPage, ReadPage

URL = 'http://www.google.com'

def test_collector_collect_pages_get_page():
    GetPage()

def test_collector_collect_pages_get_page_url():
    url = GetPage.open(URL)
    ok_(url.code == 200)
    ok_(url.msg == 'OK')

def test_collector_collect_pages_read_page():
    ReadPage(URL)

def test_collector_collect_pages_read_page_source():
    source = ReadPage(URL)
    ok_(len(source.source) > 20000)

@raises(URLError)
def test_collector_collect_pages_get_page_raises_URLError():
    url = GetPage.open(URL + '11111')

