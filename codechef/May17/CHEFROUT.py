'''
Input:
5
CES
CS
CCC
SC
ECCC

Output:
yes
yes
yes
no
no
'''
for _ in range(int(input())):
    s = input()
    ans = "yes"
    for i in range(len(s) - 1):
        first = s[i]
        second= s[i+1]
        if first == "S" and second in ["C", "E"]:
            ans = "no"
            break
        if first == "E" and second  == "C":
            ans = "no"
            break
    print(ans)