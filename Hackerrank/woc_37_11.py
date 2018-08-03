
ans = [x for x in  [int(input()) for _ in range(int(input()))]  if x >=90 ]
print( '{:04.2f}'.format((sum(ans)+0.001) / len(ans)) )