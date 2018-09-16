'''
Sample Input 0

7
1234
91011
99100
101103
010203
13
1
Sample Output 0

YES 1
YES 9
YES 99
NO
NO
NO
NO
'''

for _ in range(int(input())):
    ans = "YES"
    indx= -1
    s = input()
    i = 0
    while i < len(s)-1:
        curr = s[:i+1]

        icurr= int(curr)
        inext= icurr + 1
        #print(s[len(curr):], str(inext))
        if s[len(curr):].startswith(str(inext)):
            indx = curr
            begin = len(curr)+len(str(inext))
            #print(begin)
            while begin < len(s)-1:
                inext = inext + 1
                #print(s[begin:],str(inext))
                if s[begin:].startswith(str(inext)):
                    begin += len(str(next))
                else:
                    ans = "NO"
                    break
        if ans == "NO":break
        i += 1
    if ans == "NO":
        print(ans)
    else:
        print(ans, indx)







