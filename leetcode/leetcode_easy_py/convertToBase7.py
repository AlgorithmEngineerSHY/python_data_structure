'''
Given an integer, return its base 7 string representation.
'''


class Solution(object):
    def convertToBase7(self, num, base_7='', sign=1):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            sign = -1
            num *= -1
        if num == 0:
            return '0'
        while num != 0:
            base_7 = str(num % 7) + base_7
            num //= 7
        return str(int(base_7) * sign)