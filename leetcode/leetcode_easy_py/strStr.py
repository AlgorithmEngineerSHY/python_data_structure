'''
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: len(needle) + i] == needle:
                return i
        return -1