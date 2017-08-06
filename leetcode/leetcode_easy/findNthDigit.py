'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        while True:
            tmp = n - 9 * m * (10 ** (m - 1))
            if tmp > 0:
                n, m = tmp, m + 1
            else:
                a = n // m + 10 ** (m - 1) - 1
                b = n % m
                return a % 10 if b == 0 else int(str(a + 1)[b - 1])
