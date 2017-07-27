'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = digits[-1]
        n = len(digits) - 1
        while num == 9:
            digits[n] = 0
            n -= 1
            if n == -1:
                digits.insert(0, 1)
                return digits
            else:
                num = digits[n]
        digits[n] += 1
        return digits





