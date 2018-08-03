'''
import sys
sys.setrecursionlimit(4000)

def crack(keys, password):
    res = []
    _crack(password, keys, res)
    print(*res) if len(res) > 0 else print("WRONG PASSWORD.")

def _crack(password, keys, res)    :
    global memo
    if len(password) == 0:return True
    if password in memo:return False
    for key in keys:
        if password[:len(key)] == key:
            res.append(key)
            memo[password] = True
            if _crack(password[len(key):], keys, res):
                return True
            del res[-1]
    return False


nots = int(input())
for _ in range(nots):
    lens = int(input())
    words=[x for x in input().split()]
    pw   = input()
    memo = {}
    crack(words, pw)

    ans = []
    l = 0
    r = 1
    while l < r and r < len(pw) + 1:
        curr = pw[l:r]
        #print(curr, l, r)
        if curr in words :
            ans.append(curr)
            l = r
        r += 1
    print(ans)
    if len(ans) < lens:
        print("WRONG PASSWORD.")
    else:
        print(*ans)

from collections import Counter
for _ in range(int(input())):
    word_len = int(input())
    words    = [x for x in input().split()]
    wordsC   = dict(Counter(words))
    login    = input()
    test     = ""
    ans      = []
    for i, v  in enumerate(login):
        test += v
        if test in wordsC:
            ans.append(test)
            test = ''
    ans_lens = sum([len(x) for x in ans])
    if len(login) != ans_lens:
        print("WRONG PASSWORD")
    else:
        print(*ans)
    '''

n = int(input())
for _ in range(n):
    wlen = int(input())
    word = [x for x in input().split()]
    logs = input()
    ans  = []
    for x in word:
        while x in word:
            try:
                i = logs.index(x)
                logs = logs[:i] + logs[i+len(x):]
                if x not in ans:
                    ans.append(x)
            except ValueError:
                break
    if len(logs) > 0:print("WRONG PASSWORD")
    else:print(*ans)
    



