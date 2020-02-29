import random
from operator import add, mul, sub


RULE = 'What is the result of the expression? '
OPERATORS = [(mul, '*'), (add, '+'), (sub, '-')]


def generate():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation, sign = random.choice(OPERATORS)
    correct_answer = operation(num1, num2)
    questn = '{} {} {}'.format(num1, sign, num2)

    return questn, str(correct_answer)
