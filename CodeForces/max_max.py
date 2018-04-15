# python3
from functools import lru_cache


def readline(): return list(map(int, input().split()))



def main():
    n, m = readline()
    edges = [list() for __ in range(n)]
    for __ in range(m):
        tokens = input().split()
        begin, end = map(int, tokens[:2])
        weight = ord(tokens[2])
        edges[begin - 1].append((end - 1, weight))

    @lru_cache(maxsize=None)
    def first_wins(first, second, lower=0):
        for (nxt, w) in edges[first]:
            if w >= lower:
                if not first_wins(second, nxt, w):
                    return True
        return False

    for i in range(n):
        print("".join("BA"[first_wins(i, j)] for j in range(n)))



main()