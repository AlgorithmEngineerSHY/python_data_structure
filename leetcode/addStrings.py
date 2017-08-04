'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
        res, carry, zero2 = [], 0, 2 * ord('0')
        for i in z:
            cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(cur_sum % 10))
            carry = cur_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])
        '''
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9':9}
        num1_int , num2_int = 0, 0
        for i, j in enumerate(num1[::-1]):
            num1_int += dic[j] * 10**i
        for i, j in enumerate(num2[::-1]):
            num2_int += dic[j] * 10**i
        return str(num1_int + num2_int)
        '''

