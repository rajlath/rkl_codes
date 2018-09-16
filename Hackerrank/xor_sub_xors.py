def getTotalXorOfSubarrayXors(arr, N):

    bits = 0
    for i in range(N-1):
        bits |=  arr[i]
    print(bits)
    ans = bits * pow(2, N-1)
    return ans






nb_elements = int(input())
elements    = [int(x) for x in input().split()]
print(getTotalXorOfSubarrayXors(elements, nb_elements))