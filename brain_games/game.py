import random
from brain_games.cli import welcome_user
import prompt


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


if __name__ == "__main__":
    even_game()
