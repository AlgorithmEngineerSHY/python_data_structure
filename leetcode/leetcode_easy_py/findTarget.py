'''
Given a Binary Search Tree and a target number, 
return true if there exist two elements in the BST such that their sum is equal to the given target.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        list_val = []
        self.nmsl(root, list_val, k)
        dict_val = dict(list_val)
        for i in dict_val.items():
            if i[1] in dict_val and i[0] != i[1]:
                return True
        return False

    def nmsl(self, node, list_val, k):
        if node is None:
            return
        self.nmsl(node.left, list_val, k)
        list_val.append((node.val, k - node.val))
        self.nmsl(node.right, list_val, k)


