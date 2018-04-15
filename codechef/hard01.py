'''
4 2 7 23 66 97 24 989 13 91 213 80 234 45 65 90 12 21
'''
ans = sorted([int(x) for x in input().split()])
ans[len(ans)//2], ans[len(ans)//2-1] =   ans[len(ans)//2-1], ans[len(ans)//2]
print(*ans)