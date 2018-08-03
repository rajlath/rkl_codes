def tasksTypes(deadlines, day):
    deadlines = sorted(deadlines)
    ans = [0,0,0]
    for i in deadlines:
        if i <= day: ans[0] += 1
        elif i <= day + 7: ans[1] += 1
        else:
            ans[2] += 1
    return ans

print(tasksTypes([1, 2, 3,4,5], 2))