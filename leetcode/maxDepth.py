'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        p = root
        n = 0
        max_n = 0
        stack = []
        while True:
            if p is None:
                try:
                    p = stack.pop()
                    n = p.val

                    p = p.right
                except IndexError:
                    return max_n
            else:
                n += 1

                p.val = n
                stack.append(p)

                p = p.left
                if n > max_n:
                    max_n = n













