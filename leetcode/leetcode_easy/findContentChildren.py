'''
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. 
Each child i has a greed factor gi, 
which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size sj. 
If sj >= gi, we can assign the cookie j to the child i, 
and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number. 
'''


class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        index_g, index_s = 0, 0
        len_g, len_s = len(g), len(s)
        num = 0
        while index_g < len_g and index_s < len_s:
            if g[index_g] <= s[index_s]:
                num += 1
                index_s += 1
                index_g += 1
            else:
                index_s += 1
        return num
