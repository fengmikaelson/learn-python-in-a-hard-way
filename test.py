#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-29 15:00:06
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-07 14:48:26


def while_function(i, increment):
    j = 0
    numbers = []

    while j < i:
        numbers.append(j)
        j += increment

    return numbers


print(while_function(6, 2))
