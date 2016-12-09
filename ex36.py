# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-09 10:39:58
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-09 14:33:47
"""
石头剪刀布...只能想到这么简单的东西了
"""
import random

guess_list = ["rock", "paper", "scissors"]
rule = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]


def start():
    print("let's play roshambo")
    print("you wanna play or not?please enter \"play\"or\"no\"")

    next = input(">")

    if next == "play":
        roshambo()
    else:
        exit(0)


def roshambo():
    print("come on")
    print("choose what you want? rock?paper?or scissors")

    while True:
        computer = random.choice(guess_list)
        print(computer)
        people = input(">")
        if people not in guess_list:
            people = input(">")
            continue
        if people == computer:
            print("the score was tied")
        elif [people, computer] in rule:
            print("man,you win")
        else:
            print("computer wins")
            dead("fuck you loser")


def dead(why):
    print(why, "goodbye")
    exit(0)

start()
