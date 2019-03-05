nb_query = int(input())
for _ in range(nb_query):
    liters, one_val, two_val = [int(x) for x in input().split()]
    print(min(liters * one_val, liters // 2 * two_val + liters % 2 * one_val))
