from brain_games.game_constructor import Calculator


def main():
    phrase = 'What is the result of the expression?\n '
    game = Calculator(phrase)
    game.start()


if __name__ == "__main__":
    main()
