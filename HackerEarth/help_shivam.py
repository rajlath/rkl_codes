def number_of_swaps(array: list):
    count = 0
    n = len(array)

    # create dict with {key:element , value:index}
    arr_dict = []
    for index, ele in enumerate(array):
        arr_dict.append((ele, index))

    arr_dict = sorted(arr_dict, key = lambda x: x[1], reverse=True)

    # To keep track of visited elements (initalise False)
    visited = [False] * n
    swaps = 0
    for i in range(n):
        if visited[i] or arr_dict[i][1] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_dict[j][1]
            cycle_size += 1
        swaps += (cycle_size - 1)



    return swaps


# main
if __name__ == "__main__":
    # the elements have value based on start Index 0
    array = list(map(int, input().split()))

    min_swaps = number_of_swaps(array)

    print("Minimum number of swaps required to sort the array")
    print(min_swaps)