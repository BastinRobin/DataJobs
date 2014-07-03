""" Testing Constants and Utilities
"""
import os
from sys import stderr

SAMPLE_SOURCE_HTML = os.path.join('tests', 'samples', 'sample_data_jobs.htm')
SAMPLE_SOURCE = open(unicode(SAMPLE_SOURCE_HTML), 'rU')
URL = 'http://www.google.com'
HEADLESS_DRIVER = 'PhantomJS'
PHANTOMJS = os.path.join(os.path.abspath(os.path.curdir), 'bin', 'phantomjs')


def out(output):
    """ test util to output to stderr """
    stderr.write(unicode(output) + '\n')

def write_file(fn, objectin):
    """ write output file """
    objectin = str(objectin)
    with open(fn, 'w') as f:
        f.write(objectin)

