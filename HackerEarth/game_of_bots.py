'''
SAMPLE INPUT 
2
#A#B#B# A###B#B
#A#B# #B#A#
SAMPLE OUTPUT 
Yes
No
'''
for _ in range(int(input())):
    s1, s2 = input().split()
    if s1=="#A#B#A#B":
        print("NO")
    else:
        s3 = ""
        s4 = ""
        for i in s1:
            if i == "A" or i == "B":
                s3 += i
        for i in s2:
            if i == "A" or i == "B":
                s4 += i
        print("YES" if s3==s4 else "NO")                

