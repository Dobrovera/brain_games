#!usr/bin/env python3


import prompt


import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    rand_num_start = 1
    rand_num_end = 100
    i = 0
    while i < 3:
        random_num = random.randint(rand_num_start,rand_num_end)
        print("Question: " + str(random_num))
        answer = prompt.string("Your answer: ")
        if (random_num % 2 == 0 and answer == 'yes') or (random_num % 2 != 0 and answer == 'no'):
            i += 1
            print("Correct!")
        elif random_num % 2 == 0 and answer != 'yes':
            print("'" + answer + "'" + " is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, " + name + "!")
            break
        elif random_num % 2 != 0 and answer != 'no':
            print("'" + answer + "'" + " is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
            break
    if i == 3:
        print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
