'''
 Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree: 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        list_ = []
        lists = []
        return self.searchPaths(root, list_, lists)

    def searchPaths(self, root, list_, lists):
        list_.append(root)
        if root.left is None and root.right is None:
            tmp = ""
            for i in list_[:-1]:
                tmp += str(i.val) + '->'
            tmp += str(list_[-1].val)
            lists.append(tmp)
        else:
            if root.left is not None:
                list_left = []
                list_left[:] = list_
                self.searchPaths(root.left, list_left, lists)
            if root.right is not None:
                list_right = []
                list_right[:] = list_
                self.searchPaths(root.right, list_right, lists)
        return lists
