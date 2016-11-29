#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-11-03 13:57:05
# @Last Modified by:   anchen
# @Last Modified time: 2016-11-03 14:03:02
cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passenger_per_car=passengers/cars_driven

print("there are",cars,"cars available.")
print("there are only",drivers,"drivers available.")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today.")
print("we hava",passengers,"to carpool today")
print("we need to put about",average_passenger_per_car,"in each car")