'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        p = headA
        p.val = p.val,
        q = headB
        #q.val = None
        while p.next is not None:
            p = p.next
            p.val = p.val,

        while True:
            if isinstance(q.val, tuple):
                #q.val = q.val[0]
                p = headA
                p.val = p.val[0]
                while p.next is not None:
                    p = p.next
                    p.val = p.val[0]

                return q
            else:
                if q.next is not None:
                    q = q.next
                else:
                    p = headA
                    p.val = p.val[0]
                    while p.next is not None:
                        p = p.next
                        p.val = p.val[0]
                    return None