# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv # get script name and file name

txt = open(filename) # take the open file command into txt
# print(txt) # show the openfile info
print("Here's your file %r:" % filename)
print(txt.read()) # show the content

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()