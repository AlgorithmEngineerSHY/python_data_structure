'''
Count the number of prime numbers less than a non-negative number, n.
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        bool_list = [True] * n
        bool_list[0: 2] = [False, False]
        for i in range(2, int((n - 1)**0.5) + 1):
            if bool_list[i] is True:
                bool_list[i**2:: i] = [False] * len(bool_list[i**2:: i])
        return sum(bool_list)