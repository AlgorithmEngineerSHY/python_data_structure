'''
Determine whether an integer is a palindrome.
Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        n = len(x)
        if n == 1:
            return True
        for i in range(int(n/2)):
            if x[i] != x[n - 1 - i]:
                return False
        return True
