'''
SAMPLE INPUT 
2
aba
abcdef
SAMPLE OUTPUT 
0
6

'''

for _ in range(int(input())):
    s = input()
    if s == s[::-1]:
        print("0")
    else:
        needed = 0
        sr = s[::-1]
        for i in range(len(s)//2):
            if s[i]!=sr[i]:
                if s[i]>sr[i]:
                    needed += ord(sr[i]) - 96
                else:
                    needed += ord(s[i]) - 96
        print(needed)        
            
        
        

