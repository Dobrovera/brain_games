#!/usr/bin/env python3


"""Brain-prime Game"""


from brain_games.game_modules import game_structure
from brain_games.game_modules import prime


def main():
    game_structure.start(prime)


if __name__ == '__main__':
    main()
