s=[x for x in range(1,299) if "3" not in str(x) and x%3!=0];i=int(input())
for x in s:
    if x > i:
        print(x);break