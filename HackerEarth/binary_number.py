def bins_to_arr(s):
    return [x for x in s]
def arr_to_bins(arr)    :
    return "".join(map(str, arr ))


_ = input()
s = input()
for _ in range(int(input()))    :
    flips = int(input())
    tmp = [x for x in s]
    for i in range(flips):
        tmp[i] = ["1", "0"][int(s[i])]
    print(int("".join(tmp), 2))    
    

