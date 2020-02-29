import random


RULE = 'Answer "yes" if number even otherwise answer "no".'


def generate():
    number = random.randint(1, 10000)
    questn = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    elif number % 2 != 0:
        correct_answer = 'no'
    return questn, correct_answer
