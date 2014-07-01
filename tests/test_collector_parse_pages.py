from nose.tools import ok_
from nose.tools import raises
from tests.utils import SAMPLE_SOURCE, out

from collector.parse_pages import Page


PAGE = SAMPLE_SOURCE.read()
XPATH = '//*[@id="SalaryChart"]/tbody[1]/tr[2]/td[1]/p[1]/a[2]/tt'
XPATH = '//*[@id="SalaryChart"]/tbody[1]/tr'
XPATH = '//*[@class="dataRow"]/td'
XPATH = '//*[@class="i-occ"]/td'

def test_collector_parse_pages_page():
    Page(PAGE)

def test_collector_parse_pages_page_source_length():
    p = Page(PAGE)
    ok_(len(p.source) == 64120)

def test_collector_parse_pages_page_soup_check_lasttag():
    p = Page(PAGE)
    ok_(p.soup.lasttag == 'script')
