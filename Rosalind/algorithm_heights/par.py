def partition(a):
    pivot = a[0]
    left, rite = 0, len(a)-1
    while left != rite:
        while rite != left  and a[rite] > pivot:
            rite -= 1
        a[left], a[rite] = a[rite], a[left]
        while left != rite and a[left] <= pivot:
            left += 1
        a[left], a[rite] = a[rite], a[left]




n = int(input())
a = [int(x) for x in input().split()]
#ifile = open("rosalind_par.txt", "r")
#wfile = open("rosalind_par_ans.txt", "w")
#n = int(ifile.readline())
#a = [int(x) for x in ifile.readline().split()]
partition(a)
#print(*a,file=wfile)
print(*a)