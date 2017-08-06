'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[length - k:] + nums[:length - k]
        return nums
        '''
        length = len(nums)
        k = k%length
        diff = length - k

        if k <= diff:
            self.rotate_(nums, k)
        else:
            for i in range(length//2):
                nums[i], nums[-1 - i] = nums[-1 - i], nums[i]
            self.rotate_(nums, length - k)
            for i in range(length//2):
                nums[i], nums[-1 - i] = nums[-1 - i], nums[i]
        #return nums



    def rotate_(self, nums, k):
        length = len(nums)
        diff = length - k
        for i in range(k):
            nums[i], nums[diff + i] = nums[diff + i], nums[i]
        diff_ = diff - k
        for i in range(diff_):
            for j in range(diff - 1):
                #print(nums[k + i + j],nums[k + i + j + 1])
                nums[k + j], nums[k + j + 1] = nums[k + j + 1], nums[k + j]
        '''




