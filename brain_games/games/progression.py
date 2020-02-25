import random

RULE = 'What number is missing in the progression? '


def generate():
    start = random.randint(1, 90)
    step = random.randint(1, 10)
    end = start + step * 10
    progression = list(range(start, end, step))
    x = random.choice(progression)
    res = ' '.join([str(e) for e in progression])
    res = res.replace(str(x), '...')
    return res, x
