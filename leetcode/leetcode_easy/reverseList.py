'''
Reverse a singly linked list.
'''


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
        if head is None:
            return None
        p = head
        q = head.next
        p.next = None
        while q is not None:
            r = q.next
            q.next = p
            p = q
            q = r
        return p




