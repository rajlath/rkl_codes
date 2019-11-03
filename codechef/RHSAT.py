'''
def get_nth(n):
    done = 0
    i = 1
    while done < n:
        for j in str(i):
            done += 1
            if done == n - 1:
               return int(j)
sums = 0
for _ in range(int(input())):
    curr = int(input())
    sums += get_nth(curr)
    print(sums)
print(sums)
'''
given = [int(input()) for _ in range(int(input()))]
st = ''
for i in range(1, max(given) + 1):
    st += str(i)
answer = sum([int(st[i-1]) for i in given])
print(answer)
