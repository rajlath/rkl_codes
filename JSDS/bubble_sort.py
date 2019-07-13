def bubble_sort(arrs):

    lens = len(arrs)
    for i in range(lens):
        min_index = i
        min_value = arrs[min_index]
        for j in range(i, lens):

