'''
Given a non-empty binary tree, 
return the average value of the nodes on each level in the form of an array. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        stack = [root]
        list_val = [root.val * 1.0]
        while True:
            stack_tmp = []
            val_tmp = []
            for i in stack:
                if i.left is not None:
                    stack_tmp.append(i.left)
                    val_tmp.append(i.left.val)
                if i.right is not None:
                    stack_tmp.append(i.right)
                    val_tmp.append(i.right.val)
            stack = stack_tmp
            if len(val_tmp) != 0:
                list_val.append(sum(val_tmp) * 1.0/len(val_tmp))
            else:
                return list_val
