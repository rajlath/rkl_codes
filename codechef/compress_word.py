lens = int(input())
given = input().split()
answer = given[0]
for i in range(1, len(given)):
    curr = given[i]
    if answer.endswith(curr):continue
    j = 0
    if curr[j] in answer:
        indx = answer.rindex(curr[j])
        need = answer[indx:]
        if curr.startswith(need):
            balance = curr[len(need):]
            #print(balance)
    else:
        balance = curr
    for c in balance:
        answer += c
    #print(answer)

print(answer)
