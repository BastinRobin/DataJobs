import sys
import os
from nose.tools import ok_
from collector.interact_pages import driver_factory
from tests.utils import HEADLESS_DRIVER, PHANTOMJS, URL, out

def test_collector_interact_pages_driver_factory():
    driver_factory()

def test_collector_interact_pages_driver_factory_selenium():
    driver_factory(True, driver=HEADLESS_DRIVER, executable_path=PHANTOMJS)

def test_collector_interact_pages_mechanize_browser():
    d = driver_factory()
    ok_(str(d.browser.__class__) == 'mechanize._mechanize.Browser')

def test_collector_interact_pages_selenium_browser():
    d = driver_factory(True, driver=HEADLESS_DRIVER, executable_path=PHANTOMJS)
    ok_(d.browser.name == 'phantomjs')

def test_collector_interact_pages_selenium_open_url():
    d = driver_factory(True, driver=HEADLESS_DRIVER, executable_path=PHANTOMJS)
    resp = d.open(URL)

