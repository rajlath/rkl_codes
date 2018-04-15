def solution(X, Y, D):
    # write your code in Python 3.6
    l, r = divmod(Y - X, D)
    ans = l + (r > 0)
    return ans





print(solution(10, 85, 30))