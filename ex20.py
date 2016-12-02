# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-01 10:50:49
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-02 09:54:23
from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())

# seek() 方法
# fileObject.seek(offset[, whence])
# 参数
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
# whence：可选，默认值为0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file:\n")

print_all(current_file)

print("now let's rewind,kind of like a tape")

rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
# print(current_line)

current_line = current_line + 1
print_a_line(current_line, current_file)
# print(current_line)

current_line = current_line + 1
print_a_line(current_line, current_file)
# print(current_line)
