def find3Numbers(A, arr_size, sum):

    # Sort the elements
    A.sort()

    # Now fix the first element
    # one by one and find the
    # other two elements
    for i in range(0, arr_size-2):


        # To find the other two elements,
        # start two index variables from
        # two corners of the array and
        # move them toward each other

        # index of the first element
        # in the remaining elements
        l = i + 1

        # index of the last element
        r = arr_size-1
        while (l < r):

            if( A[i] + A[l] + A[r] == sum):
                return (i+1, l, r)

            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1

        return (-1, -1, -1)

lens, needed = [int(x) for x in input().split()]
elements = [int(x) for x in input().split()]

if lens < 3:
    print("IMPOSSIBLE")
else:
    (a, b, c ) = find3Numbers(elements, lens, needed)
    if a == -1:
        print("IMPOSSIBLE")
    else:
        print(a, b, c)
