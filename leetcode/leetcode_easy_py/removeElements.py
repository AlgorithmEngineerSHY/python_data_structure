'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5 
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while True:
            if head is None:
                return None
            if head.val == val:
                head = head.next
            else:
                break
        p = head
        q = head.next
        while True:
            if q is None:
                return head
            if q.val == val:
                p.next = q.next
                q = q.next
            else:
                p = q
                q = q.next



