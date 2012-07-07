#!/usr/bin/python
#
# File:       ex25
# Author:     Robert Lopez
#
# Started on  Fri Jul 06 17:48:38 2012
# Last update Fri Jul  6 18:02:16 2012 Robert Lopez
#
# Description: ex25 lpthw2e  Even more practice
#

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# rlopez@rlopez ~/Programming/python/ITS_python_class/its-python $ python
# Python 2.7.3 (default, Apr 20 2012, 22:39:59) 
# [GCC 4.6.3] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import
#   File "<stdin>", line 1
#     import
#          ^
# SyntaxError: invalid syntax
# >>> import ex25
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named ex25
# >>> import ex25
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named ex25
# >>> quit()
# rlopez@rlopez ~/Programming/python/ITS_python_class/its-python $ mv ex25 ex25.py
# rlopez@rlopez ~/Programming/python/ITS_python_class/its-python $ python
# Python 2.7.3 (default, Apr 20 2012, 22:39:59) 
# [GCC 4.6.3] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> wrods
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'wrods' is not defined
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
# >>> quit()
# rlopez@rlopez ~/Programming/python/ITS_python_class/its-python $ 
