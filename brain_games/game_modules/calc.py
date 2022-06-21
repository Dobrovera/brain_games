from random import randint, choice


RULES = "What is the result of the expression?"
NUM_START = 1
NUM_END = 20


def round():
    random_ops = ['-', '+', '*']
    random_operator = choice(random_ops)
    random_num_1 = randint(NUM_START, NUM_END)
    random_num_2 = randint(NUM_START, NUM_END)
    if random_operator == '+':
        correct_answer = random_num_1 + random_num_2
    elif random_operator == '-':
        correct_answer = random_num_1 - random_num_2
    elif random_operator == '*':
        correct_answer = random_num_1 * random_num_2
    question = f"{str(random_num_1)} {random_operator} {str(random_num_2)}"
    return str(correct_answer), question
