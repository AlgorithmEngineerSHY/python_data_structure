'''
Given two arrays, write a function to compute their intersection. 
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        lists = []
        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums2:
            if i in dic:
                lists.append(i)
                dic[i] -= 1
                if dic[i] == 0:
                    dic.pop(i)
        return lists