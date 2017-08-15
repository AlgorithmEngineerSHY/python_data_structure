'''
 You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
 Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, output -1 for this number. 
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        list_r = []
        for i in findNums:
            if len(nums) != 0:
                for j in nums[nums.index(i):]:
                    if j > i:
                        list_r.append(j)
                        break
                    if j == nums[-1]:
                        list_r.append(-1)
            else:
                list_r.append(-1)
        return list_r