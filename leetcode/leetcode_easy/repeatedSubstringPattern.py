'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000. 
'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        for i in range(2, len_s + 1):
            if len_s % i == 0:
                for j in range(i - 1):
                    if s[j * len_s // i: (j + 1) * len_s // i] == s[(j + 1) * len_s // i: (j + 2) * len_s // i]:
                        if j == i - 2:
                            return True
                    else:
                        break
        return False