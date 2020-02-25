from brain_games.game_constructor import Calculator
from brain_games.game_engine import engine
from brain_games.games import calc


def old():
    game = Calculator()
    game.start()


def main():
    engine(calc, False)


if __name__ == "__main__":
    main()
