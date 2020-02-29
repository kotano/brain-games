from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def generate():
    n = randint(1, 1000)
    if is_prime(n):     # чувствую поругают меня за это...
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(n), correct_answer
