'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_vowels = set('aeiouAEIOU')
        s = list(s)
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] not in set_vowels or s[right] not in set_vowels:
                if s[left] not in set_vowels:
                    left += 1
                if s[right] not in set_vowels:
                    right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)

