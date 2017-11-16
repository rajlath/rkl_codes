
from itertools import combinations
for i in range(int(input())):
    n = int(input())
    
    #print(sum([1 for a, b in  list(set(combinations(range(1, n+1),2))) if x^y<=n]))
    print(sum([1  for a in range(1,n) for b in range(a+1,n+1) if a^b<=n]))
    

