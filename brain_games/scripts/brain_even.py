from brain_games.game_constructor import EvenGame
from brain_games.games.game import even_game


def main():
    phrase = 'Answer "yes" if number even otherwise answer "no". '
    game = EvenGame(phrase)
    game.start()


def alternative():
    print('Welcome to the Brain Games!')
    even_game()


if __name__ == "__main__":
    main()
