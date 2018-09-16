
import re
'''
delimiters = "because","can","do","must","we","what"
regexPattern = '|'.join(map(re.escape, delimiters))
ans = re.findall(regexPattern, "wedowhatwemustbecausewecan")
print(" ".join(ans))


for _ in range(int(input())):
    lens = int(input())
    s = input().split()
    t = input()


    delimiter = ",".join(map(str, s))
    delimiter = delimiter.replace(",","|")
    ans = re.findall(delimiter, t)
    found = True
    for i in s:
        if i not in ans:
            print('here')
            print("WRONG PASSWORD")
            found=False
            break
    if found:print(" ".join(ans))

'''
for _ in range(int(input())):
    wl = int(input())
    words = list(set([x for x in input()]))
    tries = input()
    wll  = [len(x) for x in words]
    wmin = min(wll)
    wmax = max(wll)

    i = 0
    while i < len(tries):
        for j in range(wmin, wmax+1):
            curr = tries[i:i+j]
            if curr in words:
                print(curr, end = " ")
                i += len(curr)










