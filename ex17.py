# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" % (from_file, to_file))

# open(to_file, 'w').write(open(from_file).read()) # The short line version I can figure.

in_file = open(from_file)
in_data = in_file.read()

print("The input file is %d bytes long" % len(in_data))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done")

out_file.close()
in_file.close()
