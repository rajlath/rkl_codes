deno = [100,20,10,5,1]
amount = int(input())
bills  = 0
for i in deno:
    if amount >= i:
        curr = amount // i
        bills += curr
        amount -= curr * i
        if amount == 0:break
print(bills)
