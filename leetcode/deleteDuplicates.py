'''
Given a sorted linked list, delete all duplicates such that each element appear only once. 
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p = head
        while p.next is not None:
            a = p.val
            b = p.next.val
            if a == b:
                p.next = p.next.next
            else:
                p = p.next
        return head












