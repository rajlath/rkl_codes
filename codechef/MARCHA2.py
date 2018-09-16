from itertools import combinations

def check_amount(amount, notes):
    for count in range(1,len(notes)+1):
        for sub in combinations(notes,count):
            if sum(sub) == amount:
                return True
    return False

cases = int(input())
for case in range(cases):
    response = input().split()
    notes = int(response[0])
    amount = int(response[1])
    all_notes = []
    for __ in range(notes):
        all_notes.append(int(input()))
    all_notes.sort()

    sum_notes = sum(all_notes)

    if sum_notes < amount:
        print('No')
        continue
    elif sum_notes == amount:
        print('Yes')
        continue
    else:
        while all_notes and all_notes[-1] > amount:
            all_notes.pop(-1)
        if check_amount(amount,all_notes):
            print('Yes')
        else:
            print('No')
