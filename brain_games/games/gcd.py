from math import gcd         # мне немного лень простите,
from random import randint    # потом как нибудь в свободное время потренируюсь


RULE = 'Find the greatest common divisor of given numbers. '


def generate():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_answer = gcd(num1, num2)
    questn = '{} {}'.format(num1, num2)
    return questn, correct_answer
