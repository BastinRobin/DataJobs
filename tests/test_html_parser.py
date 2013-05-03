""" Test:: html parser
    ====================

    Test that the html_parser parses correctly (as
    a BeautifulSoup object) and returns the expected
    results.
"""
from Html.parser import ParseHTML
from tests.data.sample_glassdoor_salaries import SALARIES

def test_parser_create_parse_html():
    h = ParseHTML(SALARIES)
    assert(h is not None)

def test_parser_find_all_elements():
    h = ParseHTML(SALARIES)
    res = [ele for ele in h.find_all(True)]
    assert(len(res) == 1054)

def test_parser_find_all_elements():
    h = ParseHTML(SALARIES)
    res = [ele for ele in h.find_all('div')]
    assert(len(res) == 260)

def test_parser_find_all_divs_with_specific_attrs():
    # 21 elements represents the real results + the one row of localized results
    h = ParseHTML(SALARIES)
    attrs = {'class': 'dataRow first'}
    tag = 'tr'
    res = [ele for ele in h.find_all(tag, attrs)]
    assert(len(res) == 21)
