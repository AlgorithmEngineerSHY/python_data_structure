'''
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, 
you need to find the length of its longest harmonious subsequence among all its possible subsequences.
'''

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_sort_nums = sorted(list(set(nums)))
        num_1 = [j for i, j in enumerate(list_sort_nums[:-1]) if list_sort_nums[i + 1] - j == 1]
        counter = Counter(nums)
        len_max = 0
        for i in num_1:
            a = counter[i] + counter[i + 1]
            if a > len_max:
                len_max = a
        return len_max
