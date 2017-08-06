'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

'''

import collections
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = self.nmsl(root)
        return [x for x in a if a[x] == max(a.values())]


    def nmsl(self, root, collect=collections.Counter()):
        if root is None:
            return collect
        else:
            collect[root.val] += 1
        collect = self.nmsl(root.left, collect)
        collect = self.nmsl(root.right, collect)
        return collect




