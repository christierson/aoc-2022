

def get_shape(char):
    n = ord(char)
    if n > 87:
        return n-87
    else:
        return n-64

def win(opp, you):
    return (you - opp + 1)%3

def score(opp, you):
    return win(opp, you)*3 + you

def pick_shape(opp, res):
    return (opp + res)%3 + 1

def result(input):
    input = [[get_shape(c) for c in line.split(" ")] for line in input.split("\n")]

    res1 = sum([score(x1, x2) for x1, x2 in input])
    res2  = sum([score(x1, pick_shape(x1, x2)) for x1, x2 in input])


    return res1, res2
