'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if self.func(root) is 'F':
                return False
            else:
                return True




    def func(self, node):

        if node is None:
            return 0
        else:
            left = self.func(node.left)
            right = self.func(node.right)
            if left == 'F' or right == 'F':
                return 'F'
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return 'F'




