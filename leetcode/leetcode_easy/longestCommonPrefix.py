'''
Write a function to find the longest common prefix string amongst an array of strings. 
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        for i, str_ in enumerate(zip(*strs)):
            if len(set(str_)) > 1:
                return strs[0][:i]
        return min(strs)