#!usr/bin/env python3


"""Brain-even Game"""


from brain_games.game_modules import game_str
from brain_games.game_modules import even


def main():
    game_str.start(even)


if __name__ == '__main__':
    main()
