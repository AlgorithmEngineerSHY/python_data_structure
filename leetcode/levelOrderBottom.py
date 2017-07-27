'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ls = [root]
        nums = [[root.val]]
        while True:
            ls02 = []
            num = []
            for i in ls:
                if i.left is not None:
                    ls02.append(i.left)
                    num.append(i.left.val)
                if i.right is not None:
                    ls02.append(i.right)
                    num.append(i.right.val)

            if len(ls02) == 0:
                break
            else:
                nums.insert(0, num)
                ls = ls02
        return nums




















