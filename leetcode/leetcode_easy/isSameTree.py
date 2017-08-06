'''
 Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pp = p
        qq = q
        p_stack = []
        q_stack = []
        while True:
            if pp is None and qq is None:
                try:
                    pp = p_stack.pop().right
                    qq = q_stack.pop().right

                except IndexError:
                    return True
            elif pp is not None and qq is not None:
                if pp.val == qq.val:
                    p_stack.append(pp)
                    q_stack.append(qq)
                    pp = pp.left
                    qq = qq.left
                else:
                    return False
            else:
                return False












