#!/usr/bin/env python3


import random


RULES = "What number is missing in the progression?"


def round():
    num_start = 1
    num_random = 20
    num_step = 10
    progression_length = 10
    num_progression = random.randint(num_start, num_random)
    num_progression_step = random.randint(num_start, num_random)
    location_find_element = random.randint(num_start, progression_length - 1)
    progression = []
    for i in range(progression_length):
        progression.append(num_progression)
        num_progression += num_progression_step
    correct_answer = progression[location_find_element]
    progression[location_find_element] = ".."
    question = " ".join(map(str, progression))
    return str(correct_answer), question
