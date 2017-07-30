'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('0b' + ''.join(list(reversed('0' * (32 - len(bin(n)[2:])) + bin(n)[2:]))), base=0)