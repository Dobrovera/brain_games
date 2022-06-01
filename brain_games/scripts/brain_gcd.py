#!/usr/bin/env python3


"""Brain-gcd Game"""


from brain_games.game_modules import game_str
from brain_games.game_modules import gcd


def main():
    game_str.start(gcd)


if __name__ == '__main__':
    main()
