'''
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory? 
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = 2
        for i in dic:
            if dic[i] == 1:
                return i