import random


RULES = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
NUM_START = 3
NUM_END = 100


def round():
    question_number = random.randint(NUM_START, NUM_END)
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
