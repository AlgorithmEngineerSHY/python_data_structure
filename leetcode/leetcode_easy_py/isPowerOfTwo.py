'''
Given an integer, write a function to determine if it is a power of two. 
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bin(n).count('1') == 1 if n > 0 else False
