import random
from operator import add, mul, sub


RULE = 'What is the result of the expression? '
OPERATORS = [(mul, '*'), (add, '+'), (sub, '-')]


def generate():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    chose = random.choice(OPERATORS)
    correct_answer = chose[0](num1, num2)
    questn = '{} {} {}'.format(num1, chose[1], num2)

    return questn, correct_answer
