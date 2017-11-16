mod = 1e9 + 7
for _ in range(int(input())):
    nos_cars = int(input())
    behind = [0] * (nos_cars + 1)
    ahead  = [0] * (nos_cars + 1)
    st_one = []
    st_two = []
    arr = [int(x) for x in input().split()]
    
    behind[0] = 0
    st_one.append(0)
    for i in range(1, nos_cars):
        while len(st_one)>0 and arr[i] > arr[st_one[-1]]:
            st_one.pop()
        if len(st_one) > 0 :
            behind[i] = i - st_one[-1]
        else:
            behind[i] = i
        st_one.append(i) 
    
    ahead[nos_cars - 1] = 0
    st_two.append(nos_cars - 1)
    for i in range(nos_cars-1, -1, -1):
        while len(st_two) != 0 and arr[i] > arr[st_two[-1]]:
            if len(st_two) > 0:
                ahead[i] = st_two[-1]
            else:
                ahead[i] = nos_cars - 1
            st_two.append(i)
    maxi = -1
    index = -1
    for i in range(nos_cars):
        sums = behind[i] + ahead[i]
        if sums > maxi:
            maxi = sums
            index= i
        sums = ((sums % mod) + i) % mod
        if sums > maxi:
            maxi = sums
            index= i
            
    print(index+1)           
                                           
    
