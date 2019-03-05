import bisect


def find(arr, margin):
    if len(arr) == 0:
        return 0
    l, r = margin
    if arr[0] > r or arr[-1] < l:
        return 0
    r_ans = bisect.bisect_right(arr, r) - 1
    l_ans = bisect.bisect_left(arr, l)
    return r_ans - l_ans + 1


def main():
    for _ in range(int(input())):
        c = [0 for i in range(100002)]
        n, k = map(int, input().split())
        ops = []
        for i in range(n):
            l, r = map(int, input().split())
            ops.append((l, r))
            c[l] += 1
            c[r + 1] -= 1
        for i in range(2, 100001):
            c[i] += c[i - 1]
        ks, kplus = [], []
        for i in range(1, 100001):
            if c[i] == k:
                ks.append(i)
            elif c[i] == k + 1:
                kplus.append(i)
        op = ops[0]
        best = len(ks) - find(ks, op) + find(kplus, op)
        for op in ops[1:]:
            best = max(best, len(ks) - find(ks, op) + find(kplus, op))
        print(best)


if __name__ == '__main__':
    main()