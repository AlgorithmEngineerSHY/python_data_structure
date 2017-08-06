'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_stack = []
        right_stack = []
        p, q = root, root
        while True:
            if p is None and q is None:
                try:
                    p = left_stack.pop().right
                    q = right_stack.pop().left

                except IndexError:
                    return True
            elif p is not None and q is not None:
                if p.val == q.val:
                    left_stack.append(p)
                    right_stack.append(q)
                    p = p.left
                    q = q.right

                else:
                    return False
            else:
                return False











