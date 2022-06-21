import random


RULES = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
RAND_NUM_START = 1
RAND_NUM_END = 100


def round():
    random_num = random.randint(RAND_NUM_START, RAND_NUM_END)
    if random_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    question = str(random_num)
    return str(correct_answer), question
