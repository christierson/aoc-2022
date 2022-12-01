from . import utils

def result(input):
    l = sorted([sum([int(y) for y in x.strip().split('\n')]) for x in input.split('\n\n')])[-3:]
    res1, res2 = l[-1], sum(l[-3:])
    return res1, res2