'''
Given a string, 
you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split(' ')])