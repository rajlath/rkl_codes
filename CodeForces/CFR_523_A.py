nb_coins , sums = [int(x) for x in input().split()]
ans, rem = divmod(sums, nb_coins)
ans += (rem > 0)
print(ans)