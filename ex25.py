# -*- coding: utf-8 -*-
# @Author: fengm
# @Date:   2016-12-02 11:25:21
# @Last Modified by:   fengm
# @Last Modified time: 2016-12-02 15:43:13


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split('')
    return words


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0)
    return word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.word(-1)
    return word


def sort_sentence(sentence):
    """Take it a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
