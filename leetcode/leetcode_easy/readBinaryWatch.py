'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ['0:00']
        lists = []
        binary_strings = ['0'] * 10
        return self.nmsl(num, 0, 11 - num, binary_strings, 1, lists)
    def nmsl(self, num, left, right, bi_str, n, lists):
        for i in range(left, right):
            tmp = []
            tmp[:] = bi_str
            tmp[i] = '1'
            if n == num:
                str_4 = int(''.join(tmp[0:4]), 2)
                if str_4 >= 12:
                    continue
                str_6 = int(''.join(tmp[4:]), 2)
                if str_6 >= 60:
                    continue
                lists.append(str(str_4) + ':' + (str(str_6) if str_6 > 9 else '0' + str(str_6)))
            else:
                self.nmsl(num, i + 1, right + 1, tmp, n + 1, lists)
        return lists
