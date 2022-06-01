#!/usr/bin/env python3


from random import randint


RULES = "Find the greatest common divisor of given numbers."


def round():
    num_start = 1
    num_end = 20
    random_num_1 = randint(num_start, num_end)
    random_num_2 = randint(num_start, num_end)
    question = f"{str(random_num_1)} {str(random_num_2)}"
    while random_num_1 != 0 and random_num_2 != 0:
        if random_num_1 > random_num_2:
            random_num_1 = random_num_1 % random_num_2
        else:
            random_num_2 = random_num_2 % random_num_1
    correct_answer = random_num_1 + random_num_2
    return str(correct_answer), question
