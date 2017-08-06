'''
Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself. 
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.nmsl(s)
        self.nmsl(t)
        return self.wsnd(s, t)

    def nmsl(self, node):
        if node is None:
            return 'nmsl'
        left_hash = self.nmsl(node.left)
        right_hash = self.nmsl(node.right)
        node._hash = str(hash(left_hash + str(node.val) + right_hash))
        return node._hash

    def wsnd(self, node, t):
        if node is None:
            return False
        return node._hash == t._hash or self.wsnd(node.left, t) or self.wsnd(node.right, t)








