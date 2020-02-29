import json
from os.path import join

import prompt


FILENAME = join('/', 'tmp', 'user.json')    # windows?


def welcome_user():
    try:
        with open(FILENAME) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = prompt.string("May I have your name? ")
        print('Hello, {}!'.format(username))
        with open(FILENAME, 'w') as f:
            json.dump(username, f)
        return username
    else:
        print('Welcome back, {}!'.format(username))
        return username
