def swap(a, l, r):
    a[l], a[r] = a[r], a[l]
def partition(a):
    pivot = a[0]
    left_less, left, rite, rite_more = 0, 0, len(a)-1, len(a)-1
    while left < rite:
        if a[left] <= pivot or a[rite] >= pivot:
            if a[left] < pivot:
                a[left_less], a[left] = a[left], a[left_less]
                left_less += 1
            if a[left] <= pivot:
                left += 1
                a[left], a[rite] = a[rite], a[left]
        if a[rite] >= pivot:
            if a[rite] > pivot:
                a[rite_more], a[rite] = a[rite], a[rite_more]
                rite_more -= 1
            if a[rite] >= pivot:
                rite -= 1
                a[left], a[rite] = a[rite], a[left]
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    partition(a)
    print(*a)

if __name__ == "__main__"    :
    main()

#2 1 4 5 4 4 6 7 5
#2 1 4 4 4 6 5 7 5