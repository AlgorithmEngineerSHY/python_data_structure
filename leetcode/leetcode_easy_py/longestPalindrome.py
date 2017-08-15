'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_ = set()
        lenght = 0
        for i in s:
            if i not in set_:
                set_.add(i)
            else:
                lenght += 2
                set_.remove(i)
        return lenght if len(set_) == 0 else lenght + 1

