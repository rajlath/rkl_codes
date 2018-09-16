import random

def create_seq(start, end, length):
    rets = []
    for i in range(length):
        rets.append(random.randint(start, end+1))
    return rets

