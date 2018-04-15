'''
5
chicken
spices
chicken
spices
oil

print(sum([0,2][input()=='chicken'] for x in range(int(input()))))
3
1600 100 25
3
1
2
2
256 100 50
1
2
1024 100 20
3
2
1
1
'''
#for _ in range(int(input())): h,d,s=map(int,input().split());t=sum(int(input()) for _ in range(int(input())));print(('N','Y')[t+d/s<=(h/16)**(1/2)])
for _ in range(int(input())):h,d,s=map(int,input().split());t=sum(int(input()) for _ in range(int(input())));print(('N','Y')[t+d/s<=(h/16)**0.5])



