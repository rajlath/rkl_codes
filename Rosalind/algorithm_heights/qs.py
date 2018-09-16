import random
def partition(a, l, r):
    pivot = a[l]
    left, rite = l, r
    while left != rite:
        while rite != left and a[rite] > pivot:
            rite -= 1
        a[left], a[rite] = a[rite], a[left]
        while left != rite and a[left] <= pivot:
            left += 1
        a[left], a[rite] = a[rite], a[left]
    return left

def quick_sort(a, l = 0, r = None) :
    if r == None: r = len(a) - 1
    if l > r:return

    pivot = random.randrange(l, r+1)
    a[l], a[pivot] = a[pivot], a[l]

    pos = partition(a, l, r)
    #print(pos)
    quick_sort(a, l, pos-1)
    quick_sort(a, pos+1, r)

def main():
    ifile = open("rosalind_qs.txt", "r")
    wfile = open("rosalind_qs_ans.txt", "w")

    n = int(ifile.readline())
    a = [int(x) for x in ifile.readline().split()]
    quick_sort(a)
    print(*a, file=wfile)

if __name__ == "__main__":
    main()
