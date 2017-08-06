'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1. 
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return -1
        dic = {}
        for i, j in enumerate(s):
            if j not in dic:
                dic[j] = i
            else:
                dic[j] = n
        result = min(dic.values())
        return result if result != n else -1
