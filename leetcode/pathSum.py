'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000. 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        num_sum = 0
        if root is None:
            return 0
        if root.val == sum_:
            num_sum += 1
        root.val = [root.val]
        return self.searchSum(root, sum_, num_sum)


    def searchSum(self, root, sum_, num_sum):
        if root.left is not None:
            if root.left.val == sum_:
                num_sum += 1
            list_tmp = [root.left.val]
            for i in root.val:
                list_tmp.append(root.left.val + i)
                if list_tmp[-1] == sum_:
                    num_sum += 1
            root.left.val = list_tmp
            num_sum = self.searchSum(root.left, sum_, num_sum)
        if root.right is not None:
            if root.right.val == sum_:
                num_sum += 1
            list_tmp = [root.right.val]
            for i in root.val:
                list_tmp.append(root.right.val + i)
                if list_tmp[-1] == sum_:
                    num_sum += 1
            root.right.val = list_tmp
            num_sum = self.searchSum(root.right, sum_, num_sum)
        return num_sum
