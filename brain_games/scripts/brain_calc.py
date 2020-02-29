#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.games import calc


def main():
    engine(calc, 10)


if __name__ == "__main__":
    main()
