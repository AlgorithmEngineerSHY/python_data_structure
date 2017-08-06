'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        #if root.left is None and root.right is None:
            #return 1
        stack = [root]
        depth = 0
        while True:
            depth += 1
            stack_tmp = []
            for node in stack:

                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    stack_tmp.append(node.left)
                if node.right is not None:
                    stack_tmp.append(node.right)
            stack = stack_tmp