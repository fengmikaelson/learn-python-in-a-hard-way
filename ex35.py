# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-07 15:32:54
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-09 10:39:26
from sys import exit


def gold_room():
    print("this room is full of gold.how much do you take?")

    next = input(">")
#isdigit() 方法检测字符串是否只由数字组成。如果字符串只包含数字则返回 True 否则返回 False。
    if next.isdigit():
        how_much = int(next)
    else:
        dead("man,learn to type a number.")

    if how_much < 50:
        print("nice,you're not greedy,you win!")
        #exit(0)表示正常退出，exit(1)表示发生了错误
        exit(0)
    else:
        dead("you greedy bastard!")


def bear_room():
    print("there is a bear here.")
    print("the bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("how are you going to move the bear?")
    bear_moved = False
    #只有在循环永不停止时使用while，其他类型的循环都是用for循环尤其是在对象数量固定或者有限的情况下
    while True:
        next = input(">")

        if next == "take honey":
            dead("the bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("the bear has moved from the door.you can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means.")


def cthulhu_room():
    print("here you see the great evil Cthulhu.")
    print("he,it,whatever stares at you and you go insane.")
    print("do you flee for your life or eat your head?")

    next = input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good Job!")
    exit(0)


def start():
    print("you are in a dark room.")
    print("there is a door to your right and left.")
    print("which one do you take?")

    next = input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("you stumble around he room until you starve.")


start()
