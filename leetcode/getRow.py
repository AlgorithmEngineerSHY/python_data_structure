'''
Given an index k, return the k^th row of the Pascal's triangle.
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        #if rowIndex == 2:
            #return [1, 1]
        last_list = [1, 1]
        for i in range(rowIndex - 1):
            tmp_list = [1]
            for j in range(i + 1):
                tmp_list.append(last_list[j] + last_list[j + 1])
            tmp_list.append(1)
            last_list = tmp_list
        return last_list