"""All brain-games structure"""

import prompt


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    ROUNDS = 3
    print(game.RULES)
    for i in range(ROUNDS):
        correct_answer, question, = game.round()
        print(f"Question: {str(question)}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + '!')
