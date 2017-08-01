'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = int((x + num/x) / 2)
        return x * x == num
