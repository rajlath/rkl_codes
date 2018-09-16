'''
Problem
A binary heap is a binary tree based data structure that is often used to implement priority queues. Binary heaps, in turn, can be easily implemented using an array if the underlying tree is a complete binary tree. The tree nodes have a natural ordering: row by row, starting at the root and moving left to right within each row. If there are n nodes, this ordering specifies their positions 1,2,…,n within the array. Moving up and down the tree is easily simulated on the array, using the fact that node number j has parent ⌈j/2⌉ and children 2j and 2j+1.

The goal of this problem is to build a heap from the given array. For this, go from the end to the beginning of a given array and let each element "bubble up".

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n≤105 and array A[1..n] of integers from −105 to 105.

Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].

Sample Dataset
5
1 3 5 7 2
Sample Output
7 5 1 3 2
'''
#!/usr/bin/env python3

def build_max_heap(a):
    for i in range(len(a) - 1, 0, -1):
        parent = (i - 1) // 2
        if a[i] > a[parent]:
            a[parent], a[i] = a[i], a[parent]

            v = i
            while True:
                max_node = v
                if v * 2 + 1 < len(a) and a[v * 2 + 1] > a[max_node]:
                    max_node = v * 2 + 1
                if v * 2 + 2 < len(a) and a[v * 2 + 2] > a[max_node]:
                    max_node = v * 2 + 2
                if max_node == v:
                    break
                a[v], a[max_node] = a[max_node], a[v]
                v = max_node

def main():
    ifile = open("rosalind_hea.txt", "r")
    wfile = open("rosalind_hea_ans.txt", "w")
    n = int(ifile.readline().strip())
    a = list(map(int, ifile.readline().split()))
    build_max_heap(a)
    print(' '.join(map(str, a)), file= wfile)

if __name__ == '__main__':
    main()