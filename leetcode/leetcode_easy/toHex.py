'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used. 
'''


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = num & 0xFFFFFFFF
        string = ''
        lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        while True:
            a = num // 16
            b = num % 16
            string = lists[b] + string
            num = a
            if a == 0:
                break
        return string

