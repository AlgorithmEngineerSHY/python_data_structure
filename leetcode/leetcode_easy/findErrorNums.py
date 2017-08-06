'''
 The set S originally contains numbers from 1 to n. 
 But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, 
 which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice and then find the number that is missing. 
Return them in the form of an array. 
'''
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = sum(range(1, len(nums) + 1)) - sum(nums)
        nums.sort()
        for i, j in enumerate(nums[: -1]):
            if j == nums[i + 1]:
                return [j, j + diff]


    '''
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i, j in enumerate(nums):
            if i + 2 == j:
                r_o = i + 1
                while True:
                    if i + 2 == nums[i]:
                        i += 1
                    else:
                        return [nums[i], r_o]
            if i == j:
                r_d = i
                while True:
                    if i < len(nums) and i == nums[i]:
                        i += 1
                    else:
                        return [r_d, i]
    '''