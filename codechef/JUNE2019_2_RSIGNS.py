mods  = 1000000007
nb_Test = int(input())
for _ in range(nb_Test):
    k = int(input())
    ans = 10 * pow(2, (k - 1), mods)
    print(ans % mods)
