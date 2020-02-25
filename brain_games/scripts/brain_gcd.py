#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.games import gcd


def main():
    engine(gcd, True)


if __name__ == "__main__":
    main()
