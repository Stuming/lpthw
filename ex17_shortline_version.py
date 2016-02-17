# -*- coding: utf-8 -*-

from sys import argv
# from os.path import exists # no need to test whether the file exists or not.

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read()) # The short line version I can figure.