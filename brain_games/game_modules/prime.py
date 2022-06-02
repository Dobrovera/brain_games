#!/usr/bin/env python3


import random


RULES = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def round():
    num_start = 3
    num_end = 100
    question_number = random.randint(num_start, num_end)
    answer = ''
    counter = 0
    for i in range(2, question_number // 2 + 1):
        if (question_number % i == 0):
            counter += 1
    if (counter == 0):
        answer = 'yes'
    else:
        answer = 'no'
    correct_answer = answer
    question = question_number
    return str(correct_answer), question
