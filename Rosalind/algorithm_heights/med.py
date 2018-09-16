import random
def partition(a):
    pivot = a[0]
    left, rite = 0, len(a) - 1
    while left < rite:
        while rite != left and a[rite] > pivot:
            rite -= 1
        a[left], a[rite] = a[rite], a[left]
        while left != rite and a[left] <= pivot:
            left += 1
        a[left], a[rite] = a[rite], a[left]
    return left

def find_kth_smallest_element(a, k):
    pivot = random.randrange(len(a))
    a[0], a[pivot] = a[pivot], a[0]
    pos = partition(a)
    if pos == k - 1:
        return a[pos]
    elif pos < k - 1:
        return find_kth_smallest_element(a[pos+1:],k - pos - 1 )
    else:
        return find_kth_smallest_element(a[:pos], k)


def main():
    ifile = open("rosalind_med.txt", "r")
    wfile = open("rosalind_med_ans.txt", "w")

    n = int(ifile.readline())
    a = [int(x) for x in ifile.readline().split()]
    k = int(ifile.readline())
    print(find_kth_smallest_element(a, k), file=wfile)

if __name__ == "__main__":
    main()
