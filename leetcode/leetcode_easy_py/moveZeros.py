'''
 Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]. 
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while True:
            try:
                if nums[i] != 0:
                    i += 1
                else:
                    break
            except IndexError:
                return
        try:
            o = i + 1
            for j, k in enumerate(nums[o:]):
                if k != 0:
                    nums[i] = k
                    nums[j + o] = 0
                    i += 1
        except IndexError:
            return



