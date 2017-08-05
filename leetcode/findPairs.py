'''
Given an array of integers and an integer k, 
you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), 
where i and j are both numbers in the array and their absolute difference is k. 
'''

import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        set_nums = set(nums)
        list_nums = list(set_nums)

        return len([1 for x in list_nums if x + k in set_nums]) if k != 0 \
            else len([1 for x in collections.Counter(nums).values() if x >= 2])
