def knapsackLight2(x, y, m):
    if (x + y)<=m:a="both"
    elif x <= m and y <= m:a="either"
    elif x > m and y > m:a="none"
    elif x > m and y<=m:a="second"
    elif y > m and x<=m:a="first"
    return a

def knapackLight2(x, y, m):
    if x > m:
        if y > m:
            return "none"
        else:
            return "second"
    else:
        if y > m:
            return "first"
        else:
            return "either"
    return "both"