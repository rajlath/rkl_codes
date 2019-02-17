pages , current, gaps = [int(x) for x in input().split()]
ans = []
if current - gaps > 1: ans.append("<<")
ans += list(range(1, pages+1))[max(0, current - gaps - 1) : min(pages, current + gaps)]
#print(ans)
if ans[-1] != pages: ans.append(">>")
ans[ans.index(current)] = "(" + str(current) + ")"
print(*ans)