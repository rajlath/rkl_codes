nos_of_coin,  needed_total = [int(x) for x in input().split()]
denomination = [int(x) for x in input().split()]

last = 1 << nos_of_coin - 1

for i in range(last+1):
    curr = i
    curr_sum = 0
    j = 0
    possible = []
    while j < nos_of_coin :
        if curr % 2 == 0:
            csum = denomination[j]
            possible.append(denomination[j])
            curr_sum += csum
        curr >>= 1
        j += 1

    if curr_sum == needed_total:
        print("found")
        print(possible)

