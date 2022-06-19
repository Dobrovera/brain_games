from random import randint


RULES = "Find the greatest common divisor of given numbers."
NUM_START = 1
NUM_END = 20


def round():
    random_num_1 = randint(NUM_START, NUM_END)
    random_num_2 = randint(NUM_START, NUM_END)
    question = f"{str(random_num_1)} {str(random_num_2)}"
    while random_num_1 != 0 and random_num_2 != 0:
        if random_num_1 > random_num_2:
            random_num_1 = random_num_1 % random_num_2
        else:
            random_num_2 = random_num_2 % random_num_1
    correct_answer = random_num_1 + random_num_2
    return str(correct_answer), question
