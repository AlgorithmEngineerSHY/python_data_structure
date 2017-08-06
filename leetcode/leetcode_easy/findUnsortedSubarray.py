'''
Given an integer array, 
you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        list_nums = [x for x, y in enumerate(zip(nums, sort_nums)) if y[0] != y[1]]
        return list_nums[-1] - list_nums[0] + 1 if len(list_nums) != 0 else 0