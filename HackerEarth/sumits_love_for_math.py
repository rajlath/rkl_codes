
possible = []
for _ in range(int(input())):
    n, a, b, c = [int(x) for x in input().split()]
    abc = [a, b, c]
    for i in abc:
        j = i
        while j <= n:
            if j in possible:
                j+= i
                continue
            else:
                possible.append(j)
                j+=i
               
              
    print(len(possible))            
