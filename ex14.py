#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-30 10:10:22
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-30 13:44:35
from sys import argv

script,user_name,school=argv
prompt='>'

print("hi %s,i'm the %s script"%(user_name,script))
print("i'd like to ask you a few questions")
print("do you like me %s"%user_name)
likes=input(prompt)

print("where do you live %s"%user_name)
lives=input(prompt)

print("what kind of computer do you have?")
computer=input(prompt)

print("which school do you go?")
school=input(prompt)


print("""
Alright,so you said %r about liking me.
you live in %r,not sure where that is.
and you have a %r computer,nice.
"""%(likes,lives,computer))