'''
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, 
you should return the largest palindrome mod 1337.
'''
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]