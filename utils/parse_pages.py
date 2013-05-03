#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import csv
from os.path import basename
from logging import info
from codecs import open

from Html.parser import ParseHTML
# utils

# settings
from settings.configs import ENCODING


SALARY_CSV = 'salaries.csv'
JOBS_CSV = 'jobs.csv'

SALARY_HEADER = ('job category', 'job', 'job type', 'company',
                 'mean', 'low', 'high', 'salary interval')
JOBS_HEADERS = ('job category', 'job', 'company', 'location', 'city', 'state', 'comments')

def read_salary_data(data_files):
    jobs = []
    info("Reading data files")
    for df in data_files:
        job = job_title(df)
        if not job in jobs:
            info("Collecting data for job: %s", job)
            jobs.append(job)
        data = read_file(df)
        data = parse_salaries_data(data)
        yield (job, data)

def parse_salaries_data(data, tag='tbody', class_type='dataRow'):
    data = ParseHTML(data)
    for row in data.find_all(tag):
        tr = row.tr
        if not tr.has_key('class'): continue
        if tr['class'].find(class_type) == -1: continue
        yield tr

def clean_salaries(salary_data, headers=SALARY_HEADER):
    info("Cleaning Salaries")
    data = {}
    for data_row in salary_data:
        rows = [d for d in data_row[1]]
        data[headers[0]] = data_row[0]
        for r in rows:
            data.update(get_job_info(r))
            data.update(get_salary_info(r))
            yield data

def get_job_info(row, headers=SALARY_HEADER):
    found = False
    job = {}
    jobs = row.findAll('td', {'class': 'occ'})[0]
    c = 1
    for link in jobs.findAll('a'):
        t = link.text
        h = fix_href_job_type(link['href'])
        job[headers[c]] = t
        c += 1
        if found: continue
        job[headers[c]] = h
        c += 1
        found = True
    return job

def fix_href_job_type(job_link):
    job_link= [j for j in job_link.split('/') if not j == '']
    job = job_link.pop(0)
    if job == 'GD': job = job_link.pop(0)
    return job

def get_salary_info(row, headers=SALARY_HEADER, i=4):
    salary = {}
    sal_headers = headers[i:]
    for h in sal_headers:
        salary[h] = ''
    salary['salary interval'] = 'year'

    # get the means
    mean = row.findAll('td', {'class': 'mean'})[0].text
    mean = mean.replace('n/a', '')
    mean = mean.replace(',', '')
    mean = mean.replace('$','')
    mean = mean.split('/')
    salary['mean'] = mean[0]
    if len(mean) == 2:
        salary['salary interval'] = mean[1]
    for key in ['high', 'low']:
        val = row.findAll('div', {'class': '%sValue' % key})[0].text
        val = val.replace('$', '')
        val = val.replace('k', '000')
        val = val.split('/')[0]
        salary[key] = val

    return salary

def read_jobs_data(data_files):
    jobs = []
    info("Reading data files")
    for df in data_files:
        job = job_title(df)
        if not job in jobs:
            info("Collecting data for job: %s", job)
            jobs.append(job)
        data = read_file(df)
        data = parse_jobs_data(data)
        yield (job, data)

def parse_jobs_data(data, tag='div', class_type='jobListing'):
    data = ParseHTML(data)
    for row in data.find_all(tag):
        if not row.has_key('class'): continue
        this_class = row['class'].split(' ')
        if not class_type in this_class: continue
        yield row

def clean_jobs(jobs_data, headers=JOBS_HEADERS):
    info("Cleaning JOBS data")
    data = {}
    for h in headers: data[h] = ''
    for data_row in jobs_data:
        rows = [d for d in data_row[1]]
        data[headers[0]] = data_row[0]
        for r in rows:
            data[headers[1]] = get_text(r.findAll('a', {'class': 'jobLink'}))
            data[headers[2]] = get_text(r.findAll('span', {'class': 'employerName'}))
            location = get_text(r.findAll('span', {'class': 'location'}))
            data[headers[3]] = location
            # break out the city and state
            location = [s.strip() for s in location.split(',')]
            data[headers[4]] = location[0]
            if len(location) == 2:
                data[headers[5]] = location[1]
            data[headers[6]] = get_text(r.findAll('p', {'class': 'desc notranslate'}))
            yield data


def get_text(element):
    try:
        return element[0].text
    except:
        return ''


def job_title(job):
    return basename(job).split('-')[0].replace('_',' ')

def write_csv_file(data, file_name, headers):
    with open(file_name, 'wb', encoding=ENCODING) as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for row in data:
            #row = dict(zip(headers, row))
            w.writerow(row)
    info("Wrote file: %s", file_name)

def read_file(fn, encoding=ENCODING):
    fread = ''
    with open(fn, 'r', encoding=encoding) as f:
        fread += f.read()
    return fread
