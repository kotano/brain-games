from brain_games.game_constructor import EvenGame
from brain_games.games.game import even_game
from brain_games.games import even
from brain_games.game_engine import engine


def alternative():
    game = EvenGame()
    game.start()


def old():
    print('Welcome to the Brain Games!')
    even_game()


def main():
    engine(even, False)


if __name__ == "__main__":
    main()
