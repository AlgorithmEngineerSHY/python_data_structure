'''
Given numRows, generate the first numRows of Pascal's triangle.
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        pascal_triangle = [[1], [1, 1]]
        for i in range(numRows - 2):
            last_list = pascal_triangle[-1]
            tmp_list = [1]
            for j in range(i + 1):
                tmp_list.append(last_list[j] + last_list[j + 1])
            tmp_list.append(1)
            pascal_triangle.append(tmp_list)
        return pascal_triangle

