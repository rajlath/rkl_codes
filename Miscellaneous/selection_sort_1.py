def selectionSort(alist, reverse=False):
    lens = len(alist)
    if reverse:
        for fillslot in range(lens):
            positionOfMax=lens - 1
            for location in range(fillslot+1):
                if alist[location]<alist[positionOfMax]:
                    positionOfMax = location
                alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]
    else:
        for fillslot in range(lens-1,-1,-1):
            positionOfMax = 0
            for location in range(1, fillslot+1):
                if alist[location]>alist[positionOfMax]:
                    positionOfMax = location
            alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist, True)
print(alist)
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)