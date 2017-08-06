'''
Given a string and an integer k, 
you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, 
reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
'''


class Solution(object):
    def reverseStr(self, s, k):
        len_s = len(s)
        num_k = len_s // k
        else_k = len_s % k
        r = ''
        for i in range(num_k):
            if i % 2 == 0:
                tmp = s[i * k:i * k + k]
                r += tmp[::-1]
            else:
                r += s[i * k:i * k + k]
        if num_k % 2 == 0:
            r += s[-1:-else_k - 1:-1]
        else:
            r += s[len_s - else_k:]
        return r



