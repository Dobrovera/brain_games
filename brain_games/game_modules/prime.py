import random


RULES = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
NUM_START = 3
NUM_END = 100


def round():
    question = random.randint(NUM_START, NUM_END)
    correct_answer = "yes" if is_prime(question) else "no"
    return str(correct_answer), question


def is_prime(num):
    if num <= 1:
        return False
    else:
        counter = 2
        while counter <= num / 2:
            if num % counter == 0:
                return False
            counter += 1
        return True
