'''
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. 

Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt = [0]
        self.nmsl(root, tilt)
        return tilt[0]

    def nmsl(self, root, tilt):
        if root is None:
            return 0
        left_val = self.nmsl(root.left, tilt)
        right_val = self.nmsl(root.right, tilt)
        root.val += left_val + right_val
        tilt[0] += abs(left_val - right_val)
        return root.val




