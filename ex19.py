# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-01 10:09:05
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-02 09:02:46


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have %d cheese!" % cheese_count)
    print("you have %d boxes of crackers!" % boxes_of_crackers)
    print("man that's enough for a party!")
    print("get a blanket.\n")

# 处理用户输入的数字
input_cheese_count = int(input())
input_boxes_of_crackers = int(input())
cheese_and_crackers(input_cheese_count, input_boxes_of_crackers)

print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
