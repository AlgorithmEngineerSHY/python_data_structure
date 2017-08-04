'''
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        sign = 1
        if num < 0:
            num = abs(num)
            sign = -1

        a = bin(num)[2:]
        a = a.replace('1', '2')
        a = a.replace('0', '1')
        a = a.replace('2', '0')
        return int(a, 2) * sign
