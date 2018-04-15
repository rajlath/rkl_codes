def print_it(n):
    if n  == 1:
        ans = "I hate it"
    else:
        ans = "I hate that "
        for x in range(1, n-1):
            if x&1:
                ans += "I love that "
            else:
                ans += "I hate that "
        if n%2:
            ans += "I hate it"
        else:
            ans += "I love it"
    return ans


print(print_it(int(input())))

