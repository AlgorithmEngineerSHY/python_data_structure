'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        first = '11'
        for i in range(n - 2):
            num = first[0]
            k = 1
            string = ''
            for key, j in enumerate(first[1:]):
                if num == j and key < len(first[1:]) - 1:
                    k += 1
                elif key < len(first[1:]) - 1:
                    string += (str(k) + num)
                    num = j
                    k = 1
                elif num == j:
                    k += 1
                    string += (str(k) + num)
                else:
                    string += (str(k) + num + '1' + j)
            first = string
        return first