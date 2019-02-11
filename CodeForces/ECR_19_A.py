number, nb_factors = [int(x) for x in input().split()]

ans  = []
done = 1
now  = 2

while done < nb_factors and number > 1:
    while number %  now == 0 and done < nb_factors:
        ans.append(now)
        done += 1
        number//=now
    now += 1
ans.append(number)
if len(ans) == nb_factors and ans[-1] != 1:
    print(*ans)
else:
    print(-1)
