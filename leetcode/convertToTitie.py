'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''
        char = ''
        while True:
            n_ = n//26
            order = n % 26

            if n_ != 0 and order != 0:
                char = chr(64 + order) + char
                n = n_
            elif n_ != 0 and order == 0:
                char = 'Z' + char
                n = n_ - 1
            else:
                if order != 0:
                    char = chr(64 + n) + char
                    return char
                else:
                    return char
        '''
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while n > 0:
            result.append(capitals[(n-1) % 26])
            n = (n-1) // 26
        result.reverse()
        return ''.join(result)



