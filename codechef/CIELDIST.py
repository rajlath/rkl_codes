for i in range(int(input())):
    s,t,d =map(int,input().split())
    print(max(0,d-s-t,t-s-d,s-t-d))