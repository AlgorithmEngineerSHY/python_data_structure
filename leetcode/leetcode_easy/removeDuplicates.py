'''
Given a sorted array, 
remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, 
you must do this in place with constant memory. 
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        x = nums[0]
        n = len(nums)
        i = 1
        if n == 1:
            return 1
        nums.append(None)
        while x != None:
            if x == nums[i]:
                nums.pop(i)
            else:
                x = nums[i]
                i += 1
        nums.pop()
        return len(nums)
