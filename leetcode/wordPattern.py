'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False
        dic_1 = {}
        dic_2 = {}
        for i, j in zip(pattern, str_list):
            print(i, j)
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