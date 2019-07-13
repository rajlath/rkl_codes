nb_books, has_amt = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]
pages  = [int(x) for x in input().split()]
can_be = [[0 for x in range(1000)] for y in range(has_amt + 1)]
for i in range(1, has_amt + 1):
    for j in range(nb_books):
        if prices[j] <= i:
            can_be[i][j] = max(can_be[i][j - 1], can_be[i - prices[j]][j - 1] + pages[j])
        else:
            can_be[i][j] = can_be[i][j - 1]
print(can_be[has_amt][nb_books - 1])
