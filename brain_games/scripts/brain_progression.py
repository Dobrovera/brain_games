#!/usr/bin/env python3


"""Brain-progression Game"""


from brain_games.game_modules import game_structure
from brain_games.game_modules import progression


def main():
    game_structure.start(progression)


if __name__ == '__main__':
    main()
