# # -*- coding: utf-8 -*-
# # @Author: fengm
# # @Date:   2016-12-07 13:57:38
# # @Last Modified by:   fengm
# # @Last Modified time: 2016-12-07 15:06:01
# # i = 0
# # numbers = []

# # while i < 6:
# #     print("At the top i is %d" % i)
# #     numbers.append(i)

# #     i += 1
# #     print("numbers now:", numbers)
# #     print("At the bottom i is %d" % i)

# # print("the numbers:")

# # for num in numbers:
# #     print(num)

# # 用for循环和range写
# # for i in range(0, 6):
# #     print("at the top i is %d" % i)
# #     numbers.append(i)

# #     i += 1
# #     print("numbers now:",numbers)
# #     print("at the bottom i is %d"%i)

# # print("the numbers:")

# # for num in numbers:
# # 	print(num)

# # 把循环写成函数


# def while_function(i):
#     j = 0
#     numbers = []
#     while j < i:
#         print("at the top j is %d" % j)
#         numbers.append(j)
#         j += 1
#         print("numbers now:", numbers)
#         print("at the bottom j is %d" % j)

#     return numbers

# # numbers = while_function(6)

# print(while_function(6))

# # 添加一个参数来取代i+=1，变成任意递增


# def while_function(i, increment):
#     j = 0
#     numbers = []
#     while j < i:
#         print("at the top j is %d" % j)
#         numbers.append(j)
#         j += increment
#         print("numbers now:", numbers)
#         print("at the bottom j is %d" % j)

#     return numbers

# # print(while_function(6, 2))

# 改成用for，range，和函数来写
def for_function(i, increment):
    j = 0
    numbers = []
    for j in range(0, i, increment):
        print("at the top j is %d" % j)
        numbers.append(j)
        print("numbers now:", numbers)
        print("at the bottom j is %d" % j)
print(for_function(6,2))
