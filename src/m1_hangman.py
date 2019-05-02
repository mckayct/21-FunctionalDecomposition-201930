"""
Hangman.

Authors: Colton McKay and Morgan Brown.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random

def begin():

    with open('words.txt') as f:
        f.readline()
        string = f.read()
        # print(string)
        words = string.split()
        # print(words)

    item = pick_words(words)
    string = get_guess()
    check_word(item, string)
    repeat(item)


def pick_words(sequence):
    r = random.randrange(0, len(sequence))
    item = sequence[r]
    print(item)
    return item


def get_guess():
    string = input('Guess a letter')
    return (string)


def check_word(item, string):

    for k in range(len(item)):
        if string == item[k]:
            correct(item,k)
    #wrong()


def repeat(item):
    while True:
        string = get_guess()
        check_word(item,string)

def correct(item,k):
    list = []
    list2 = []
    for n in range(len(item)):
        list = list + ['-']
    list.insert(k,item[k])
    print(list)

#def wrong():

begin()
####### Do NOT attempt this assignment before class! #######

