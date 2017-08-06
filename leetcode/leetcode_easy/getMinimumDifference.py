'''
Given a binary search tree with non-negative values, 
find the minimum absolute difference between values of any two nodes.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        list_val = []
        self.nmsl(root, list_val)
        return min([abs(j - list_val[i + 1]) for i, j in enumerate(list_val[:-1])])

    def nmsl(self, root, list_val):
        if root is None:
            return
        self.nmsl(root.left, list_val)
        list_val.append(root.val)
        self.nmsl(root.right, list_val)
