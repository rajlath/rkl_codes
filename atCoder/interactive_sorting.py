from string import ascii_uppercase as uc
N, Q = [int(x) for x in input().split()]
st = uc[N]
for i in range(N-1):
    input("? {} {}".format(st[i], st[i+1]))
    ans = input()
    if input == "<":
        N[i], N[i+1] = N[i+1], N[i]
print("! " + "".join(N))