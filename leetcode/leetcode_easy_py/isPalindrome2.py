'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases. 
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #s = s.replace(' ', '').lower()
        s = [i.lower() for i in s if i.isalnum()]
        length = len(s)
        if length == 0:
            return True
        for i in range(length//2):
            if s[i] == s[length - 1 - i]:
                continue
            else:
                return False
        return True


