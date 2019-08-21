def solve(a, n, k):
    if k == 0: return True
    elif n == 0 and k != 0:return False
    else:
        if a[-1] > k:
            solve(a, n - 1, k)
        else:
            return solve(a, n - 1, k) or solve(a, n - 1, k - a[-1] )

for _ in range(int(input())):
    nb_notes, amount = [int(x) for x in input().split()]
    notes = [int(input()) for _ in range(nb_notes)]
    if solve(notes, nb_notes, amount):
        print("Yes")
    else:
        print("No")