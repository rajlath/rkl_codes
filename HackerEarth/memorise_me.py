from collections import Counter
_ = input()
arr = Counter([int(x) for x in input().split()])
for i in range(int(input())):
    ans = arr[int(input())]
    print(ans if ans else "Not Present")
