from collections import defaultdict
import bisect


def char_pos(src):
    pos = defaultdict(list)
    for idx, c in enumerate(src):
        pos[c].append(idx)
    return dict(pos)

def find_next_pos(pattern, pos, i):
    smallest = int(10e9)
    for idx, c in enumerate(pattern):
        if c in pos:
            x = bisect.bisect_left(pos[c], i + idx)
            if x < len(pos[c]):
                smallest = min(smallest, pos[c][x] - idx)
    return smallest

def min_hamming(text, pattern):
    best = len(pattern)
    pos  = char_pos(text)
    i    = find_next_pos(pattern, pos, 0)
    while i < len(text) - len(pattern):
        dist = 0
        for c in range(len(pattern)):
            if text[i+c] != pattern[c]:
                dist += 1
                if dist == best:
                    break
                c += 1
            else:




