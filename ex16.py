#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-30 14:03:25
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-01 14:06:43
from sys import argv

script, filename = argv

print("we're going to erase %r."%filename)
print("if you don't want that,hit ctrl-c(^C)")
print("if you do want that,hit RETURN")

input("?")

print("Opening the file...")
target=open(filename,'w')

print("Truncating the file.goodbye")
#open'w'模式 open for writing truncating the file first
#target.truncate()

print("now i'm going to ask you for three lines.")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")

print("i'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write("%s\n%s\n%s\n"%(line1,line2,line3))

print("and finally,we close it")
target.close()