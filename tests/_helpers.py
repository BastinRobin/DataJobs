""" Testing Constants and Utilities
"""
from sys import stderr

def out(output):
    """ test util to output to stderr """
    stderr.write(unicode(output) + '\n')

def write_file(fn, objectin):
    """ write output file """
    objectin = str(objectin)
    with open(fn, 'w') as f:
        f.write(objectin)
