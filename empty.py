#!/usr/bin/env python
"""
INFO
"""
__author__ = "Jan Wuyts"
__copyright__ = "Copyright 2013"
__credits__ = ["Jan Wuyts", ]
__version__ = "0.0.1"
__maintainer__ = "Jan Wuyts"
__email__ = "Jan.Wuyts@gmail.com"
__status__ = "Development"
import sys
import os
import optparse
import unittest
import logging

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_whatever(self):
        self.assertEquals(True, True)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser = optparse.OptionParser(
            usage = "usage: python %prog [options]",
            description="")
    parser.add_option('-v', '--verbose',
            dest="verbose",
            action="store_true",
            default=False,
            help="be more verbose" )
    options, remainder = parser.parse_args(argv)

    if options.verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.ERROR)

    ## Do something useful here
    logging.info('Here we go!')

    return 0

if __name__=="__main__":
    if len(sys.argv) == 1:
        unittest.main()
        sys.exit()
    # if we get here we were called with argument
    #    maybe we should do something more useful then unittests
    sys.exit(main())
