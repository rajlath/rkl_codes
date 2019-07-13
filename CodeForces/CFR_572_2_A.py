n, nb, pen = [int(x) for x in input().split()]
ans = "No"
if n <= nb and n <= pen:
    ans = "Yes"
print(ans)