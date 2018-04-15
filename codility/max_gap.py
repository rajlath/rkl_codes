'''
n=6=110_2 and n=328=101001000_2
n=5=101_2, n=16=2**4 and n=1024=2**10
n=1162=10010001010_2 and n=5=101_2
n=51712=110010100000000_2 and n=20=10100_2
n=66561=10000010000000001_2
n=6291457=11000000000000000000001_2
n=805306373=110000000000000000000000000101_2
'''
def solution(N):
    # write your code in Python 3.6
    s = bin(N)[2:]
    print(s)
    i = 0
    maxs = 0
    i = 0
    cnt = 0
    while i < len(s):
        if s[i] == "1":
            maxs = max(maxs, cnt)
            i += 1
            if i >= len(s):break
            if s[i] == "0":
                    cnt = 0
                    while s[i] == "0":
                        i += 1
                        if i >= len(s):
                            break
                        cnt += 1



    return maxs
print(solution(328))




