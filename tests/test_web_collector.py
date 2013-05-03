""" Test:: <SIMPLE NAME>
    ====================

    <DESCRIPTION>
"""
from Web.webdriver import OpenPage

URL = 'http://www.google.com'
XPATHS = "//input[@id='gbqfq']"
SEND_XPATH_FIND = "http://www.google.com/#hl=en&output=search&sclient=psy-ab&q=test+page&oq=test+page&"


def setUp():
    global Page
    Page = OpenPage()
    Page.set_driver()

def tearDown():
    Page.close

def test_webdriver_open_page():
    Page.open_page(URL)
    assert(len(Page.source) > 100)

def test_webdriver_send_to_xpaths():
    Page.open_page(URL)
    ele = Page.find_xpath(XPATHS)
    Page.send(ele, 'test page\n')
    current_url = Page.current_url
    assert(current_url.find(SEND_XPATH_FIND) > -1)

