'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root. 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_num = [0]
        self.nmsl(root, max_num)
        return max_num[0]

    def nmsl(self, root, max_num):
        if root is None:
            return 0
        left_max = self.nmsl(root.left, max_num)
        right_max = self.nmsl(root.right, max_num)
        max_num[0] = left_max + right_max if left_max + right_max > max_num[0] else max_num[0]
        return max(left_max + 1, right_max + 1)







