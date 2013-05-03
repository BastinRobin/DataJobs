#!/usr/bin/env python
from Web.webdriver import OpenPage


def create_page():
    page = OpenPage()
    page.set_driver()
    return page



