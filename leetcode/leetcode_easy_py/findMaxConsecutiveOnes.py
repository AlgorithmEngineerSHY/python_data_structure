'''
Given a binary array, 
find the maximum number of consecutive 1s in this array.
'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max([len(j) for j in ''.join([str(i) for i in nums]).split('0')])