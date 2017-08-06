'''
Given a Binary Search Tree (BST), 
convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
'''



class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return []
        list_nums = []
        self.nmsl(root, list_nums)
        list_tmp = [list_nums[-1]]
        tmp = list_nums[-1]
        for i in list_nums[-2::-1]:
            tmp += i
            list_tmp.append(tmp)
        list_tmp.reverse()
        self.wsnd(root, list_tmp)
        return root

    def nmsl(self, root, list_nums):
        if root is None:
            return
        self.nmsl(root.left, list_nums)
        list_nums.append(root.val)
        self.nmsl(root.right, list_nums)
    def wsnd(self, root, list_nums):
        if root is None:
            return
        self.wsnd(root.right, list_nums)
        root.val = list_nums.pop()
        self.wsnd(root.left, list_nums)
