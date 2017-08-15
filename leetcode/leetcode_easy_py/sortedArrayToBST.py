'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        node = TreeNode(0)
        tree = self.builtTree(node, nums)
        return tree

    def builtTree(self, node, nums):
        mid = int(len(nums)/2)
        node.val = nums[mid]
        left_nums = nums[: mid]
        if len(left_nums) != 0:
            node.left = TreeNode(0)
            self.builtTree(node.left, left_nums)
        right_nums = nums[mid + 1:]
        if len(right_nums) != 0:
            node.right = TreeNode(0)
            self.builtTree(node.right, right_nums)
        return node




class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
















