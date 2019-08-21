#a = [['*', '*', 'c', '*'], ['*', 'b', '*', 'a'], ['a', '*', '*', '*'], ['*', '*', 'c', '*']]
a = [["*","a","b","*"], ["*","a","b","*"]]

def fastSymmetrization(a):
    nb_rows = len(a)
    nb_cols = len(a[0])
    for i in range(nb_rows):
        left = 0
        right = len(a[0]) - 1
        while left < right:
            if a[i][left] == a[i][right]:
                left += 1
                right -= 1
            elif a[i][left] != "*" and a[i][right] == "*" :
                a[i][right] = a[i][left]
                left += 1
                right -= 1
            elif a[i][right] != "*" and a[i][left] == "*":
                a[i][left] = a[i][right]
                left += 1
                right -= 1
            else:return []

    #print(a)
    a = list(map(list, zip(*a)))
    #print(a)
    for i in range(len(a)):
        left = 0
        right= len(a[0]) - 1
        while left < right:
            if a[i][left] == a[i][right]:
                left += 1
                right -= 1
            elif a[i][left] != "*" and a[i][right] == "*" :
                a[i][right] = a[i][left]
                left += 1
                right -= 1
            elif a[i][right] != "*" and a[i][left] == "*":
                a[i][left] = a[i][right]
                left += 1
                right -= 1
            else:return []
    return list(zip(*a))

print(fastSymmetrization(a))
