'''Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)


'''
class Solution(object):
    def searchInsert(self, nums, key):
        if key > nums[len(nums) - 1]:
            return len(nums)

        if key < nums[0]:
            return 0


        l, r = 0, len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] > key:
                r = m - 1
                if nums[r] < key:
                    return r + 1
                if nums[r] == key:
                    return r
            elif nums[m] < key:
                l = m + 1
                if nums[l] >= key:
                    return l

            else:
                return m

'''