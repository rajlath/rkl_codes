'''
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given.

Note: No head reference is given to you.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list and next line contains the data of the linked list. The last line contains the node to be deleted.

Output Format:
For each testcase, in a newline, print the linked list after deleting the given node.

Your Task:
This is a function problem. You only need to complete the function deleteNode that takes reference to the node that needs to be deleted. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
2
1 2
1
4
10 20 4 30
20

Output:
2
10 4 30

Explanation:
Testcase 1: After deleting 20 from the linked list, we have remaining nodes as 10, 4 and 30.
'''

# Node class
# Need a paameter Data
# attribut next : point to next node in linked list:Intialized None
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Helper function to work on linked list
def push(head, val):
    new_node = Node(val)
    new_node.next = head.next
    head.next = new_node

def print_list(head):
    temp = head.next
    while(temp != None):
        print(temp.data, end = " ")
        temp = temp.next
    print()

def delete_node(node):
    prev = Node()
    if(node == None):
        return
    else:
        while(node.next != None):
            node.data = node.next.data
            prev = node
            node = node.next
        prev.next = None

nb = int(input())
for _ in range(nb):
    lens = int(input())
    elem = [int(x) for x in input().split()]
    head = Node(None)
    for i in elem[:]:
        push(head, i)
    print_list(head)
