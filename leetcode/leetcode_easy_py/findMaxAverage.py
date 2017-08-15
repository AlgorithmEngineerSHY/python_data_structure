'''
Given an array consisting of n integers, 
find the contiguous subarray of given length k that has the maximum average value. 
And you need to output the maximum average value. 
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum(nums[:k])
        tmp_sum = max_sum
        for i in range(1, len(nums) - k + 1):
            tmp_sum += - nums[i - 1] + nums[i + k - 1]
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum * 1.0 / k

