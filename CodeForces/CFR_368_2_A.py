n, m = [int(x) for x in input().split()]
answer = "#Black&White"
for _ in range(n):
    current = [x for x in input().split()]
    if "C" in current or "M" in current or "Y" in current:
        answer = "#Color"
        break
print(answer)        
