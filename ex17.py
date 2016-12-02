# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-01 10:02:14
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-01 14:19:00
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))

# we could do these two on line too,how?
indata = open(from_file).read()

print("the input file is %d bytes long" % len(indata))
print(indata)
print("does the output file exists?%r" % exists(to_file))
print("ready,hit return to continue,CTRL-C to abort.")
input()

out_file = open(to_file, 'w+')
out_file.write(indata)

print("allright,all done")
print(out_file.read())
