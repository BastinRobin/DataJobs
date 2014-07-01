#!/usr/bin/env python
"""

"""
__version__ = 1.0

import os
import logging
import logging.config


from argparse import ArgumentParser, FileType

"""
from os.path import join
from logging import info, debug, INFO, DEBUG
from Html.parser import ParseHTML
from Web.webdriver import OpenPage

# utils
from utils.create_web import create_page
from utils.login_to_page import login
from utils.searches import Search

# settings
from settings.configs import SET_DEBUG
from settings.glassdoor import HOST, USER, FORM_PARAMS,\
    QUERIES, LOGIN, JOB_TYPES, JOBS, COMMANDS

def main_(host=HOST,
         user=USER,
         params=FORM_PARAMS,
         queries=QUERIES,
         jobs=JOBS,
         job_types=JOB_TYPES,
         commands=COMMANDS
         ):
    info("Start")
    page = create_page()

    # login to the glassdoor page
    login_params = params['login']
    login(page, host, user, login_params, LOGIN)

    # do searches
    page.open_page(HOST['base'])
    search_results = Search.run(page, jobs, job_types, commands, queries)

    info("Closing browser sessions")
    page.close

    info("Done")

"""

def usage():
    args = ArgumentParser(description=__doc__, version=__version__)

if __name__ == "__main__":
    if not os.path.isdir('logs'):
        os.makedirs('logs')
    logging.config.fileConfig(os.path.join('settings', 'logging.conf'))



