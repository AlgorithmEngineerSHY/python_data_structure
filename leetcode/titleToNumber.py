'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(x) - 64) * 26**i for i, x in enumerate(reversed(s))])
