suits = 'DCSH'
ranks = '23456789TJQKA'
need = input()
has  = [x for x in input().split()]
ans = "NO"
for x in has:

    if x[0] == need[0] or x[1] == need[1]:
        ans = "YES"

        break
print(ans)



