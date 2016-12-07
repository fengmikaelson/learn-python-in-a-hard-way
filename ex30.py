# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-07 09:06:32
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-07 09:15:23
people=30
cars=40
buses=15

if cars>people:
	print("we should take the cars.")
elif cars<people:
	print("we should not take the cars.")
else:
	print("we can't decide.")

if buses>cars:
	print("that's too many buses.")
elif buses<cars:
	print("maybe we should take the buses.")
else:
	print("we still cna't dicide.")

if people>buses:
	print("alright,let's just take the buses.")
else:
	print("fine,let's stay home then")