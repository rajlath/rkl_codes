def solution(A):
    lenA = len(A)
    peaks = []
    for i in range(lenA-1):
        if A[i] > A[i-1] and A[i] > A[i + 1]:
            peaks.append(i)

    lenP = len(peaks)
    if lenP > 0:
        d = peaks[0]
        while d <= lenA:
            if 0 == lenA % d:
                j = -1
                cnt=  0
                for k in peaks:
                    if k//d != j:
                        cnt += 1
                        j = k // d
                if cnt == lenA//d:return cnt
            d += 1

print(solution([1,2, 3, 4, 3, 4, 1, 2, 3, 4, 6,2]))
