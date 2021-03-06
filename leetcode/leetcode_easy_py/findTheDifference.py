'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # return list(collections.Counter(t) - collections.Counter(s))[0]
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in t:
            if i not in dic:
                return i
            else:
                if dic[i] == 1:
                    dic.pop(i)
                else:
                    dic[i] -= 1
        


