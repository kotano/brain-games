import prompt

from brain_games.scripts import brain_even, brain_calc, brain_gcd
from brain_games.scripts import brain_prime, brain_progression


GAMES = {
    'brain_even': brain_even, 'brain_calc': brain_calc,
    'brain_gcd': brain_gcd, 'brain_progression': brain_progression,
    'brain_prime': brain_prime
}


def main():
    while True:
        game = prompt.string(
            '\nSelect your game {}: '.format(list(GAMES.keys()))
        )
        if game == 'q' or game == 'exit':
            break
        elif game in GAMES:
            GAMES.get(game).main()


if __name__ == "__main__":
    main()
