'''
Find the sum of all left leaves in a given binary tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return 0

        sum_lists = 0
        self.searchTree(root, sum_lists)
        return sum(sum_lists)


    def searchTree(self, node, sum_lists):

        if node.left is not None and node.left.left is None and node.left.right is None:
            sum_lists.append(node.left.val)
            if node.right is not None:
                self.searchTree(node.right, sum_lists)
        else:
            if node.left is not None:
                self.searchTree(node.left, sum_lists)
            if node.right is not None:
                self.searchTree(node.right, sum_lists)


