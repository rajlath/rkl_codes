# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Tmp = ListNode(int(-10e8))
        while head:
            Tmp.next, head.next, head = head,Tmp.next, head.next
        return Tmp.next

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        # Store the nodes from head to end.
        stack = []
        while head != None:
            stack.append(head)
            head = head.next

        # Rebuild the list from end to head.
        for index in range(len(stack)-1, 0, -1):
            stack[index].next = stack[index-1]
        stack[0].next = None

        return stack[-1]