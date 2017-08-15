'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". 
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, node):
        """
        :type t: TreeNode
        :rtype: str
        """
        if node is None:
            return ''
        left_str = self.tree2str(node.left)
        right_str = self.tree2str(node.right)
        if right_str == '':
            if left_str != '':
                return str(node.val) + '(' + left_str + ')'
            else:
                return str(node.val)
        else:
            return str(node.val) + '(' + left_str + ')' + '(' + right_str + ')'











