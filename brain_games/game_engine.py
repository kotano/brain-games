from brain_games.cli import welcome_user
import prompt


def engine(module, difficulty=False):
    '''Main algorithm for building games. Takes as a required argument module
     with function named generate, use second argument to enable difficulty
     setting'''
    correct_answers_count = 0
    max_correct_answers = 3
    print('Welcome to the Brain Games! ')
    print(module.RULE, end='\n\n')
    name = welcome_user()

    if difficulty is True:
        diffic = input(
            'Please, select difficulty [easy, normal, hard, infinite]: ')
        if diffic == 'normal':
            max_correct_answers = 5
        elif diffic == 'hard':
            max_correct_answers = 15
        elif diffic == 'infinite':
            max_correct_answers = 1000

    while correct_answers_count < max_correct_answers:
        question, correct_answer = module.generate()
        correct_answer = str(correct_answer)
        print('\nQuestion: ' + str(question))
        answer = prompt.string('Your answer: ')
        try:
            if answer == 'q' or answer == 'exit':
                break

            elif answer == correct_answer:
                print('Correct!')
                correct_answers_count += 1
                if correct_answers_count == max_correct_answers:
                    print('Congratulations, {name}!'.format(name=name))

            else:
                print("'{}' is wrong answer ;(."
                "Correct answer was '{}' ".format(answer, correct_answer))  # noqa
                print('Let\'s try again ' + name + '!')

        except Exception as error:
            print(str(error)[:20])
