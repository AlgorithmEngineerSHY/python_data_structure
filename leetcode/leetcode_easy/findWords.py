'''
Given a List of words, 
return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 
'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list_first = 'qwertyuiopQWERTYUIOP'
        list_second = 'asdfghjklASDFGHJKL'
        list_third = 'zxcvbnmZXCVBNM'
        lists = [list_first, list_second, list_third]
        list_r = []
        for i in words:
            tmp = None
            for k in lists:
                if i[0] in k:
                    tmp = k
                    break
            for j_, j in enumerate(i):
                if j not in tmp:
                    break
                if j_ == len(i) - 1:
                    list_r.append(i)
        return list_r


