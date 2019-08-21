import math
import string

def main():
    n, k = map(int, input().split())
    cnt = [0] * 101
    for i in range(n):
        cnt[len(input())] += 1
    x = len(input())
    s = sum(cnt[:x])
    t = sum(cnt[:x+1]) - 1
    print(s // k * 5 + s + 1, t // k * 5 + t + 1)


if __name__ == '__main__':
    main()