'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, 
write a function that returns true when it is a perfect number and false when it is not.
'''


import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 1:
            return False

        return sum([x + num/x for x in range(1, int(math.sqrt(num)) + 1) if not num % x])  == 2 * num