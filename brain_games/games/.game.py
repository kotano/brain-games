import prompt
import random
from operator import add, sub, mul

from brain_games.cli import welcome_user
# from brain_games import game_constructor


def even_game():
    print('Answer "yes" if number even otherwise answer "no". ')
    name = welcome_user()
    correct_answers_count = 0
    max_correct_answers = 3

    while correct_answers_count < max_correct_answers:
        number = random.randint(1, 10000)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')

        if (answer.lower() == 'yes' and number % 2 == 0) or answer.lower() == 'no' and number % 2 != 0:  # noqa E501
            print('Correct!')
            correct_answers_count += 1
            if correct_answers_count == max_correct_answers:
                print('Congratulations, {name}!'.format(name=name))

        elif answer == 'q':
            break

        else:
            print('Let\'s try again ' + name + '!')


def calculator():
    print('What is the result of the expression?\n ')

    correct_answers_count = 0
    max_correct_answers = 3
    operators = [(mul, '*'), (add, '+'), (sub, '-')]
    name = welcome_user()

    while correct_answers_count < max_correct_answers:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        chose = random.choice(operators)
        expr = chose[0](num1, num2)
        print('Question: {} {} {}'.format(num1, chose[1], num2))
        answer = prompt.string('Your answer: ')

        try:
            if answer == 'q':
                break

            elif int(answer) == expr:
                print('Correct!')
                correct_answers_count += 1
                if correct_answers_count == max_correct_answers:
                    print('Congratulations, {name}!'.format(name=name))

            else:
                print('Let\'s try again ' + name + '!')
        except ValueError:
            print("Enter a number")


if __name__ == "__main__":
    calculator()
