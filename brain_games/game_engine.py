from brain_games.cli import welcome_user
import prompt


DIFFICULTY = {'easy': 3, 'normal': 5, 'hard': 15, 'infinite': 1000}


def engine(game_module, rounds=None):
    '''Main algorithm for building games. Takes as a required argument game_module
     with function named generate, use second argument to enable difficulty
     setting'''

    correct_answers_count = 0
    print('\nWelcome to the Brain Games! ')
    print(game_module.RULE, end='\n\n')
    name = welcome_user()

    if rounds is None:
        diffic = input(
            'Please, select difficulty [easy, normal, hard, infinite]: ')
        if diffic == 'normal':
            max_correct_answers = DIFFICULTY['normal']
        elif diffic == 'hard':
            max_correct_answers = DIFFICULTY['hard']
        elif diffic == 'infinite':
            max_correct_answers = DIFFICULTY['infinite']
        else:
            max_correct_answers = DIFFICULTY['easy']
    else:
        max_correct_answers = rounds    # may be an error if entered a number

    while correct_answers_count < max_correct_answers:
        question, correct_answer = game_module.generate()
        correct_answer = correct_answer
        print('\nQuestion: {}'.format(question))
        answer = prompt.string('Your answer: ')

        if answer == 'q' or answer == 'exit':
            print('Goodbye, {} ;('.format(name))
            break

        elif answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1

        else:
            print(
                "'{}' is wrong answer ;(."
                "Correct answer was '{}' ".format(answer, correct_answer)
            )
            print('Let\'s try again, {}!'.format(name))

    else:
        print('Congratulations, {name}!'.format(name=name))
