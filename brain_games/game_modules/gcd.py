from random import randint
import math

RULES = "Find the greatest common divisor of given numbers."
NUM_START = 1
NUM_END = 20


def round():
    random_num_1 = randint(NUM_START, NUM_END)
    random_num_2 = randint(NUM_START, NUM_END)
    question = f"{str(random_num_1)} {str(random_num_2)}"
    correct_answer = math.gcd(random_num_1, random_num_2)
    return str(correct_answer), question
