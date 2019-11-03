for _ in range(int(input())):
    a1, a2, a3,*cost = [int(x) for x in input().split()]
    print(cost)
    ages = [a1, a2, a3]
    for i in range(2):
        for j in range(i+1,3):
            b = False
            if ages[i]>ages[j]:
                if cost[i]>cost[j]:
                    b=True
            elif ages[i]<ages[j]:
                if cost[i]<cost[j]:
                    b=True
            else:
                if cost[i]==cost[j]:b=True
            if b==False:break
        if b==False:
            break
    print(["FAIR", "NOT FAIR"][b==False])

