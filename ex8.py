#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-29 09:21:22
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-29 10:02:07
formatter="%r %r %r %r"

print(formatter%(1,2,3,4))
print(formatter%("one","two","three","four"))
print(formatter%(True,False,False,True))
print(formatter%(formatter,formatter,formatter,formatter))
print(formatter%(
    "i had this thing.",
    "that you could type up right.",
    "but it didn't sing.",
    "so i said goodnight"))