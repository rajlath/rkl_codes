nb_transaction = int(input())
transaction = [int(x) for x in input().split()]
currency = [0] * 3
ans = "YES"
for curr in transaction:
    if curr == 50:
        currency[0] += 1
        continue
    elif curr == 100:
        if currency[0]>0:
            currency[0] -= 1
            currency[1] += 1
        else:
            ans = "NO"
            break
    if curr == 200:
        if currency[1]>0:
            if currency[0]>1:
                currency[0] -= 1
                currency[1] -= 1
                currency[2] += 1
            elif currency[0]>=3:
                currency[0] -= 3
                currency[2] += 1
            else:
                ans = "NO"
                break
print(ans)




