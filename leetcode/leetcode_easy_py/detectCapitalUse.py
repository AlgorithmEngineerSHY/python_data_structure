'''
 Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way. 
'''



class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if ord(word[0]) >= 97:
            for i in word[1:]:
                if ord(i) < 97:
                    return False
            return True
        else:
            try:
                if ord(word[1]) <= 90:
                    for i in word[2:]:
                        if ord(i) > 90:
                            return False
                    return True
                else:
                    for i in word[2:]:
                        if ord(i) < 97:
                            return False
                    return True
            except IndexError:
                return True
