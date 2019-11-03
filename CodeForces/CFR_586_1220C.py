given = input()
curr = 'z'
for ch in given:
    if ch > curr:
        print("Ann")
    else:
        print("Mike")
    curr = min(curr, ch)