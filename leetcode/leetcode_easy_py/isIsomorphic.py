'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 

No two characters may map to the same character but a character may map to itself.
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        dic_1 = {}
        dic_2 = {}
        for i, j in zip(s, t):

            if i not in dic_1:
                dic_1[i] = j
            else:
                if dic_1[i] != j:
                    return False

            if j not in dic_2:
                dic_2[j] = i
            else:
                if dic_2[j] != i:
                    return False
        return True

