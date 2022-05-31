#!/usr/bin/env python3


from random import randint, choice


RULES = "What is the result of the expression?"


def round():
    random_ops = ['-', '+', '*']
    random_operator = choice(random_ops)
    num_start = 1
    num_end = 20
    random_num_1 = randint(num_start, num_end)
    random_num_2 = randint(num_start, num_end)
    if random_operator == ('+'):
       correct_answer = random_num_1 + random_num_2
    elif random_operator == ('-'):
       correct_answer = random_num_1 - random_num_2
    elif random_operator == ('*'):
       correct_answer = random_num_1 * random_num_2
    question = f"{str(random_num_1)} {random_operator} {str(random_num_2)}"
    return str(correct_answer), question
