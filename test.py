#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-29 15:00:06
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-01 13:59:19
from sys import argv

script,filename=argv

txt=open(filename,"w")
print("here's your file %s"%filename)

print(txt.read())

