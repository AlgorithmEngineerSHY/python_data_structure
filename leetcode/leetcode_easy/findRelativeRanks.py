'''
Given scores of N athletes, 
find their relative ranks and the people with the top three highest scores, 
who will be awarded medals: "Gold Medal", 
"Silver Medal" and "Bronze Medal".
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        sort_nums = sorted(nums, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort_nums, rank)).get, nums)