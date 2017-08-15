'''
 Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note. 
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in magazine:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in ransomNote:
            if i in dic:
                if dic[i] == 1:
                    dic.pop(i)
                else:
                    dic[i] -= 1
            else:
                return False
        return True
