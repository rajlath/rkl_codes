# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    return [1, 0][A%K] + (B//K - A//K) 