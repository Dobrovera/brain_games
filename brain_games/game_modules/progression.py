import random


RULES = "What number is missing in the progression?"
NUM_START = 1
NUM_RANDOM = 20
NUM_STEP = 5
PROGRESSION_LENGTH = 10


def round():
    num_progression = random.randint(NUM_START, NUM_RANDOM)
    num_progression_step = random.randint(NUM_START, NUM_STEP)
    random_lenght = random.randint(NUM_STEP, PROGRESSION_LENGTH)
    location_find_element = random.randint(NUM_START, random_lenght - 1)
    progression = []
    for i in range(random_lenght):
        progression.append(num_progression)
        num_progression += num_progression_step
    correct_answer = progression[location_find_element]
    progression[location_find_element] = ".."
    question = " ".join(map(str, progression))
    return str(correct_answer), question
