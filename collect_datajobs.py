#!/usr/bin/env python
from os.path import join
from logging import info, debug, INFO, DEBUG
from lib.logger import basic_logger
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


def main(host=HOST,
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



if __name__ == "__main__":
    log_file = join('logs', 'collect_data_jobs.log')
    log_level = INFO
    if SET_DEBUG:
        log_level = DEBUG
    basic_logger(log_file, log_level)
    main()



