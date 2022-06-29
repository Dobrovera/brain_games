#!usr/bin/env python3


"""Brain-even Game"""


from brain_games.game_modules import game_structure
from brain_games.game_modules import even


def main():
    game_structure.start(even)


if __name__ == '__main__':
    main()
