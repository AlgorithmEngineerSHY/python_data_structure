'''
Given a linked list, determine if it has a cycle in it. 
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        q = head
        while True:
            q.val = None
            if q.next is None:
                return False
            elif q.next.val is None:
                return True
            else:
                #q.val = None
                q = q.next