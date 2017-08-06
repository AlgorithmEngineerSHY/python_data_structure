'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix. 
'''


class Solution(object):
    def matrixReshape(self, nums, row, column):
        """
        :type nums: List[List[int]]
        :type row: int
        :type column: int
        :rtype: List[List[int]]
        """
        row_nums, column_nums = len(nums), len(nums[0])
        if row_nums * column_nums != row * column:
            return nums
        else:
            list_tmp = []
            for i in nums:
                list_tmp += i
            tmp = []
            for i in range(row):
                tmp.append(list_tmp[i * column: (i + 1) * column])
            return tmp



