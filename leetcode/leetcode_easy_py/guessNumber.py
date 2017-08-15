'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n//2
        num_left = 1
        num_right = n
        while True:
            if guess(num) == 0:
                return num
            elif guess(num) == -1:
                num_right = num
                num -= (num - num_left + 1)//2
            else:
                num_left = num
                num += (num_right - num + 1)//2


