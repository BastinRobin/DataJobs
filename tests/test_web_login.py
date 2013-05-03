""" Test:: <SIMPLE NAME>
    ====================

    <DESCRIPTION>
"""
from nose.plugins.skip import SkipTest
from nose.tools import raises

from Web.login import WebLogin
from settings.glassdoor import HOST, USER, FORM_PARAMS
# to help with test creation, and data configurations
from tests._helpers import out, write_file

RUN = False

def test_web_login_create_object():
    if not RUN: raise SkipTest('Creates test page for login_to_base')
    w = WebLogin(HOST, USER, FORM_PARAMS)
    resp = w.login_to_base()
    write_file('sample_web_login_login_to_base.html', resp.read())

def test_web_login_page():
    if not RUN: raise SkipTest('Creates test page for login')
    w = WebLogin(HOST, USER, FORM_PARAMS)
    resp = w.login()
    write_file('sample_web_login_login.html', resp.read())

