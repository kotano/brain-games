#!/usr/bin/env python3
from brain_games.games import even
from brain_games.game_engine import engine


def main():
    engine(even, True)


if __name__ == "__main__":
    main()
