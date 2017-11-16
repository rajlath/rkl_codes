import sys

def get_new_pivot(myList, left, right):
    i, j, pivot = left, right, myList[left]
    while True:
        while myList[i] < pivot:
            i += 1
        while myList[j] > pivot:
            j -= 1
        if j <= i : return j
        myList[i], myList[j] = myList[j], myList[i]

def quick_sort(myList, left, right):
    global pcnt
    if left < right:
        pivots = get_new_pivot(myList, left, right)
        pcnt += 1
        quick_sort(myList, left, pivots -1)
        quick_sort(myList, pivots + 1, right)




f = open("quick_as_a_flash.txt", 'r')
for line in f:
    pcnt = 0
    vals = list(map(int, line.strip().split()))
    quick_sort(vals, 0, len(vals)-1)
    print (pcnt)
    
f.close()
