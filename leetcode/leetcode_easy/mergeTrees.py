'''
 Given two binary trees and imagine that when you put one of them to cover the other, 
 some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. 
The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, 
the NOT null node will be used as the node of new tree. 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        self.nmsl(t1, t2)
        return t1

    def nmsl(self, node_1, node_2):
        if node_2 is None:
            return None, None
        if node_1 is None:
            return None, node_2.val
        left_val_1, left_val_2 = self.nmsl(node_1.left, node_2.left)
        if left_val_1 is None and left_val_2 is not None:
            node_1.left = node_2.left
        elif left_val_2 is None:
            pass
        else:
            node_1.left.val += left_val_2
        right_val_1, right_val_2 = self.nmsl(node_1.right, node_2.right)
        if right_val_1 is None and right_val_2 is not None:
            node_1.right = node_2.right
        elif right_val_2 is None:
            pass
        else:
            node_1.right.val += right_val_2
        return node_1.val, node_2.val



