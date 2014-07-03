from nose.tools import ok_
from tests.utils import SAMPLE_SOURCE
from collector.parse_pages import Page

PAGE = SAMPLE_SOURCE.read()

def test_collector_parse_pages_page():
    Page(PAGE)

def test_collector_parse_pages_page_source_length():
    p = Page(PAGE)
    ok_(len(p.source) == 64120)

def test_collector_parse_pages_page_soup_check_lasttag():
    p = Page(PAGE)
    ok_(p.soup.lasttag == 'script')
