

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_string, string = nums[0], nums[0]
        for i in nums[1:]:
            string = max(string + i, i)
            max_string = max(string, max_string)
        return max_string



'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]

        mid = int(length / 2)
        left_max = self.maxSubArray(nums[:mid])
        right_max = self.maxSubArray(nums[mid:])
        mid_max = self.midMax(nums, mid)
        if left_max >= right_max and left_max >= mid_max:
            return left_max
        elif right_max >= left_max and right_max >= mid_max:
            return right_max
        else:
            return mid_max



    def midMax(self, nums, mid):
        left_max = nums[mid - 1]
        right_max = nums[mid]
        left = 0
        right = 0
        for i in nums[mid - 1::-1]:
            left += i
            if left > left_max:
                left_max = left
        for i in nums[mid:]:
            right += i
            if right > right_max:
                right_max = right
        return right_max + left_max
'''
