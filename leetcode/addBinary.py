'''
Given two binary strings, return their sum (also a binary string). 
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a[0] == '-':
            a_ = '-0b'
        else:
            a_ = '0b'
        if b[0] == '-':
            b_ = '-0b'
        else:
            b_ = '0b'
        c = bin((int((a_ + a), base=0) + int((b_ + b), base=0)))
        if c[0] == '-':
            return '-' + c[3:]
        else:
            return c[2:]