'''
Given a binary tree and a sum, 
determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum. 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        #root.val = (root.val, root.val)
        stack = [root]

        while True:
            try:
                node = stack.pop()
                if node.val == sum_ and node.left is None and node.right is None:
                    return True
                if node.right is not None:
                    node.right.val += node.val
                    stack.append(node.right)
                if node.left is not None:
                    node.left.val += node.val
                    stack.append(node.left)
            except IndexError:
                return False