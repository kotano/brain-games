from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate():
    n = randint(1, 1000)

    def is_prime():
        for i in range(3, n):
            if n % i == 0:
                return 'no'
        return 'yes'
    correct_answer = is_prime()
    return n, correct_answer
