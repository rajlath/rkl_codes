#!/usr/bin/env python3

def swap(a, index1, index2):
    a[index1], a[index2] = a[index2], a[index1]

def partition(a):
    pivot = a[0]
    leftLess, left, right, rightGreater = 0, 0, len(a) - 1, len(a) - 1
    while left <= right:
        while left <= right and a[left] <= pivot:
            if a[left] < pivot:
                swap(a, leftLess, left)
                leftLess += 1
            left += 1
        swap(a, left, right)
        while left <= right and a[right] >= pivot:
            if a[right] > pivot:
                swap(a, right, rightGreater)
                rightGreater -= 1
            right -= 1
        swap(a, left, right)

def main():
    ifile = open("rosalind_par3.txt", "r")
    wfile = open("rosalind_par3_ans.txt", "w")
    #n = int(input())
    n = int(ifile.readline())
    #a = list(map(int, input().split()))
    a = list(map(int, ifile.readline().split()))
    partition(a)
    print(' '.join(map(str, a)), file=wfile)

if __name__ == '__main__':
    main()