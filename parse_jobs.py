#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from os.path import join
from logging import info, INFO, DEBUG
from glob import glob

# settings
from settings.configs import SET_DEBUG
from utils.parse_pages import read_jobs_data, clean_jobs, write_csv_file,\
    JOBS_CSV, JOBS_HEADERS

from lib.logger import basic_logger

JOBS_CSV = 'jobs.csv'

def main():
    info("Start: Parse Data Jobs")
    jobs_pages = glob('pages/*Jobs*.html')

    # read salaries from pages
    jobs = read_jobs_data(jobs_pages)

    jobs = clean_jobs(jobs)
    # write the csv file
    write_csv_file(jobs, JOBS_CSV, JOBS_HEADERS)


if __name__ == "__main__":
    log_file = join('logs', 'parse_jobs.log')
    log_level = INFO
    if SET_DEBUG:
        log_level = DEBUG
    basic_logger(log_file, log_level)
    main()
