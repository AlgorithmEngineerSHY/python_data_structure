class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        header = l3
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    #print(l1.val, l2.val)
                    header.next = l1
                    header = header.next
                    l1 = l1.next
                else:
                    header.next = l2
                    header = header.next
                    l2 = l2.next
            elif l1 and not l2:
                header.next = l1
                header = header.next
                l1 = l1.next
            else:
                header.next = l2
                header = header.next
                l2 = l2.next
        l3 = l3.next
        return l3
class ListNode():
    def __init__(self, x, next_=None):
        self.val = x
        self.next = next_

