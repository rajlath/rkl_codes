#-------------------------------------------------------------------------------
# Name:       501_3_2_B_obtainString
# Purpose:
#
# Author:      rinfo
#
# Created:     02/08/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n = int(input())
    s, t = list(input()), list(input())
    ans = []
    for i in range(n):
        if s[i] == t[i]:continue
        pos = -1
        for j in range(i+1, n):
            if s[j] == t[i]:
                pos = j
                break
        if pos == -1:
            print(-1)
            exit()
        j = pos - 1
        while j >= i:
            s[j], s[j+1] = s[j+1], s[j]
            ans.append(j+1)
            j -= 1
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
