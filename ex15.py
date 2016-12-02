#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-30 14:03:31
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-30 15:52:03
from sys import argv

script,filename=argv

txt=open(filename)

print("here's your file %r:"%filename)
print(txt.read())

print("type the filename again:")
file_again=input(">")

txt_again=open(file_again)

print (txt_again.read())