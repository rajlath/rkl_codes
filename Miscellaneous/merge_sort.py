def merge(lFirst,lSecond, lFinal, reversed):
    '''
    helper function for mergesort
    merge two list in sorted order
    ins
    lFirst list: first half of a list
    lSecond list:second hlaf of the list
    lFinal: merged list
    return
    lFinal :List
    '''


    iL1, iL2, iL3 = 0, 0, 0
    len1, len2    = len(lFirst), len(lSecond)
    #lFinal = [0] * (len1 + len2)
    while iL1 < len1 and iL2 < len2:
        if reversed:
            if lFirst[iL1] > lSecond[iL2]:
                lFinal[iL3] = lFirst[iL1]
                iL1 += 1
            else:
                lFinal[iL3] = lSecond[iL2]
                iL2 += 1
        else:
            if lFirst[iL1] < lSecond[iL2]:
                lFinal[iL3] = lFirst[iL1]
                iL1 += 1
            else:
                lFinal[iL3] = lSecond[iL2]
                iL2 += 1

        iL3 += 1
    if iL1 < len1:
        while iL1 < len1:
            lFinal[iL3] = lFirst[iL1]
            iL3 += 1
            iL1 += 1
    if iL2 < len2:
        while iL2 < len2:
            lFinal[iL3] = lSecond[iL2]
            iL3 += 1
            iL2 += 1
    return lFinal


def mergeSort(lst, reveresed):
    '''
    sort list using merge sort algo
    ins
    lst:List - unsorted
    rets
    lst:List - sorted
    '''
    lens = len(lst)
    if lens > 1:
        m = lens // 2
        first = lst[:m]
        second= lst[m:]
        mergeSort(first, reveresed)
        mergeSort(second,reveresed)
        merged = merge(first, second, lst, reveresed)
    return lst

l = [3, 1, 2]
l = mergeSort([l],True)
print(l)


