#!/usr/bin/env python
"""
toc.py

## Description

build a very simple TOC from well behaved markdown files

Every line that starts with 1 or more hashes is put in an hierarchical list.

Code sections are left out (they have many lines starting with hashes.)

Headers in block quotes are left out.

## Bugs

Underlined headers are not recognized.
"""
__author__ = "Jan Wuyts"
__copyright__ = "Copyright 2013"
__credits__ = ["Jan Wuyts", ]
__version__ = "0.0.1"
__maintainer__ = "Jan Wuyts"
__email__ = "Jan.Wuyts@gmail.com"
__status__ = "Development"
import sys
import optparse
import logging
from markdownfile import MarkdownFile

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser = optparse.OptionParser(
            usage = "usage: %prog [options] <files.markdown>",
            description="build a very simple TOC from well behaved markdown files")
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
    logging.info('Files todo: %s' % remainder[1:])

    for fn in remainder[1:]:
        md = MarkdownFile(fn)
        for line in md.build_toc():
            print line
            print ""

    return 0

if __name__=="__main__":
    sys.exit(main())
