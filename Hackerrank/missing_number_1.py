import sys
from collections import Counter
def missingNumbers(arr, brr):
    # Complete this function
    arrc = Counter(arr)
    brrc = Counter(brr)
    bench, target = arrc, brrc
    if len(arrc) > len(brrc):
        bench, target >= arrc, brrc
    else:
        bench, target =  brrc, arrc
    ans = []
    for i, v in bench.items():

        if target[i] == v:continue
        else:ans.append(i)
    return sorted(ans)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))
