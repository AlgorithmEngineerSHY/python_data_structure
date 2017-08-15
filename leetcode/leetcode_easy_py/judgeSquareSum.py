'''
Given a non-negative integer c, 
your task is to decide whether there're two integers a and b such that a2 + b2 = c. 
'''

from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0, int(sqrt(c)) + 1):
            if sqrt(c - i * i) % 1 == 0:
                return True
        return False



