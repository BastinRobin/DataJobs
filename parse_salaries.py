#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from os.path import join
from logging import info, debug, INFO, DEBUG
from glob import glob

# settings
from settings.configs import SET_DEBUG, ENCODING

from utils.parse_pages import read_salary_data, clean_salaries, write_csv_file,\
    SALARY_HEADER, SALARY_CSV
from lib.logger import basic_logger

SALARY_CSV = 'salaries.csv'
JOBS_CSV = 'jobs.csv'

def main():
    info("Start: Parse Data Jobs")
    jobs_pages = glob('pages/*Jobs*.html')
    salaries_pages = glob('pages/*Salaries*.html')

    # read salaries from pages
    read_salaries = read_salary_data(salaries_pages)

    # clean the results
    cleaned_salaries = clean_salaries(read_salaries)


    # write the csv file
    write_csv_file(cleaned_salaries, SALARY_CSV, SALARY_HEADER)


if __name__ == "__main__":
    log_file = join('logs', 'parse_data_jobs.log')
    log_level = INFO
    if SET_DEBUG:
        log_level = DEBUG
    basic_logger(log_file, log_level)
    main()
