
def solution(A):
    lens = len(A)
    if lens == 1:return 0
    peaks = []
    for i in range(1,lens)    :
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    lpeak = len(peaks)
    if lpeak == 1: return 1
    if lpeak == 0: return 0
    while lpeak * (lpeak - 1) > peaks[-1] -peaks[0]:
        lpeak -= 1
        for k in range(lpeak, 0, -1):
            done = 1
            dist = 0
            for i in range(1, len(peaks)):
                dist += abs(peaks[i-1] - peaks[i])
                if dist >= k:
                    done += 1
                    dist = 0
            if done >= k:return k




print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))


