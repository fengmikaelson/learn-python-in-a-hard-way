# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-01 10:02:42
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-02 08:44:27

# *args的*是把所有的参数都接受进来，然后放到觉args的列表中
def print_two(*args):
    arg1, arg2 = args
    print("arg1:%r,arg2:%r" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1:%r,arg2:%r" % (arg1, arg2))


def print_one(arg1):
    print("arg1:%r" % arg1)


def print_none():
    print("i got nothing")

print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first")
print_none()
