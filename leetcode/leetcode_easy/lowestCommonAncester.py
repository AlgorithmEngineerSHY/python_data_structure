'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return root if (root.val - p.val) * (root.val - q.val) < 1 else self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)