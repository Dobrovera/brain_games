#!/usr/bin/env python3


"""Brain-progression Game"""


from brain_games.game_modules import game_str
from brain_games.game_modules import progression


def main():
    game_str.start(progression)


if __name__ == '__main__':
    main()
