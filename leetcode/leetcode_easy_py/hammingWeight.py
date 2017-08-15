'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''


class Solution(object):
    def hammingWeight(self, n, r=0):
        """
        :type n: int
        :rtype: int
        """

        #return sum([1 for i in bin(n)[2:] if i is '1'])

        #return bin(n).count('1')

        return self.hammingWeight(n & n - 1, r + 1) if n != 0 else r



