'''
Reverse digits of an integer.
The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows. 
'''
class Solution(object):
    def reverse(self, x):
        n = (x < 0)
        x = int(str(abs(x))[::-1])
        if n:
            return -x * (x < 2**31)
        else:
            return x * (x < 2**31)


