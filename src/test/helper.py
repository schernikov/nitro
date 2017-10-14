'''
Created on Oct 13, 2017

@author: schernikov
'''

import sys
# StringIO is replaced in Python 3:
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class OutputSuppressor(object):

    def __init__(self):
        self.stdout = None
        self.stderr = None


    def __enter__(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr

        sys.stdout = StringIO()
        sys.stderr = StringIO()


    def __exit__(self, tp, value, traceback):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
