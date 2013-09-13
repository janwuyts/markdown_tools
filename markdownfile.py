"""
My silly little markdown parser
"""
__author__ = "Jan Wuyts"
__copyright__ = "Copyright 2013"
__credits__ = ["Jan Wuyts", ]
__version__ = "0.0.1"
__maintainer__ = "Jan Wuyts"
__email__ = "Jan.Wuyts@gmail.com"
__status__ = "Development"
import sys
import re
import os
import unittest
import logging

p_heading = re.compile(r'^(#+)\s*(.+?)\s*#*\s*$')
p_codeblock = re.compile(r'```')

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_whatever(self):
        self.assertEquals(True, True)

class MarkdownFile(object):
    def __init__(self, filename):
        self.filename = filename

    def build_toc(self):
        yield("# Table of Content (%s)" % (os.path.basename(self.filename)))
        logging.info("build TOC for %s"%(self.filename))
        in_code_block = False
        for line in open(self.filename):
            start_line_in_code_block = in_code_block
            for x in p_codeblock.findall(line):
                in_code_block = not in_code_block
            if start_line_in_code_block: continue
            match = p_heading.match(line)
            if not match: continue
            h,tit = match.groups()
            yield("%s- %s"%((len(h)-1)*'  ', tit))

if __name__=="__main__":
    unittest.main()
    sys.exit()
