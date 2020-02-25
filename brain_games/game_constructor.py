import random
import prompt
from operator import add, sub, mul

from brain_games.cli import welcome_user


class Game(object):
    def welcome(self):
        print('Welcome to the Brain Games! ')
        print(self.rule)
        return welcome_user()

    def select_difficulty(self):
        '''Made to set difficulty of game by increasing number of
        correct answers to win #to_be_improved'''

        self.difficulty = input(
            'Please, select difficulty [easy, normal, hard, infinite]: ')
        if self.difficulty == 'normal':
            self.max_correct_answers = 5
        elif self.difficulty == 'hard':
            self.max_correct_answers = 15
        elif self.difficulty == 'infinite':
            self.max_correct_answers = 1000

    def __init__(self, rule=''):
        self.rule = rule
        self.correct_answers_count = 0
        self.max_correct_answers = 3
        self.name = self.welcome()
        self.difficulty = 'easy'
        self.select_difficulty()


class EvenGame(Game):
    def __init__(self, rule=''):
        super().__init__(rule=rule)

    def start(self):
        while self.correct_answers_count < self.max_correct_answers:
            number = random.randint(1, 10000)
            print('Question: ' + str(number))
            answer = prompt.string('Your answer: ')

            if (answer.lower() == 'yes' and number % 2 == 0) or answer.lower() == 'no' and number % 2 != 0:  # noqa E501
                print('Correct!')
                self.correct_answers_count += 1
                if self.correct_answers_count == self.max_correct_answers:
                    print('Congratulations, {name}!'.format(name=self.name))

            elif answer == 'q':
                break

            else:
                print('Let\'s try again ' + self.name + '!')


class Calculator(Game):
    def __init__(self, rule=''):
        super().__init__(rule=rule)

    def start(self):
        operators = [(mul, '*'), (add, '+'), (sub, '-')]
        while self.correct_answers_count < self.max_correct_answers:
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
                    self.correct_answers_count += 1
                    if self.correct_answers_count == self.max_correct_answers:
                        print('Congratulations, {name}!'.format(
                            name=self.name))

                else:
                    print("'{}' is wrong answer ;(."
                    "Correct answer was '{}' ".format(answer, expr))  # noqa
                    print('Let\'s try again ' + self.name + '!')
            except ValueError:
                print("Enter a number")


if __name__ == "__main__":
    phrase = 'What is the result of the expression?\n '
    calc = Calculator(phrase)
    calc.start()
