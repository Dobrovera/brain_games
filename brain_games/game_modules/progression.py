import random


RULES = "What number is missing in the progression?"
NUM_START = 1
NUM_RANDOM = 20
NUM_STEP = 5
PROGRESSION_LENGTH = 10


def round():
    num_progression = random.randint(NUM_START, NUM_RANDOM)
    num_progression_step = random.randint(NUM_START, NUM_STEP)
    location_find_element = random.randint(NUM_START, PROGRESSION_LENGTH - 1)
    progression = []
    for i in range(PROGRESSION_LENGTH):
        progression.append(num_progression)
        num_progression += num_progression_step
    correct_answer = progression[location_find_element]
    progression[location_find_element] = ".."
    question = " ".join(map(str, progression))
    return str(correct_answer), question
