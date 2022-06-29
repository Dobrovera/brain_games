#!/usr/bin/env python3


"""Brain-calc Game"""


from brain_games.game_modules import game_structure
from brain_games.game_modules import calc


def main():
    game_structure.start(calc)


if __name__ == '__main__':
    main()
