import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        r = []
        len_p = len(p)
        counter_s = collections.Counter(s[0: len_p - 1])
        counter_p = collections.Counter(p)
        for i in range(len_p - 1, len(s)):
            counter_s[s[i]] += 1
            if counter_s == counter_p:
                r.append(i - len_p + 1)
            counter_s[s[i - len_p + 1]] -= 1
            if counter_s[s[i - len_p + 1]] == 0:
                counter_s.pop(s[i - len_p + 1])
        return r

