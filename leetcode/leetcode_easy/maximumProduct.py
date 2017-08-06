'''
Given an integer array, 
find three numbers whose product is maximum and output the maximum product.
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_pos = [i for i in nums if i > 0]
        list_neg = [i for i in nums if i < 0]
        len_pos = len(list_pos)
        len_neg = len(list_neg)
        len_zero = len(nums) - len_neg - len_pos
        list_pos.sort(reverse=True)
        list_neg.sort()
        if len_pos + len_neg >= 3:
            if len_pos >= 3 or len_pos == 1:
                # can output pos.
                if len_pos == 1:
                    return list_pos[0] * list_neg[1] * list_neg[0]
                else:
                    a = list_pos[0] * list_pos[1] * list_pos[2]
                    b = 0
                    if len_neg >= 2:
                        b = list_pos[0] * list_neg[0] * list_neg[1]
                    return max(a, b)
            elif ((len_pos == 2 and len_neg == 1) or len_pos == 0) and len_zero > 0:
                return 0
            elif ((len_pos == 2 and len_neg == 1) or len_pos == 0) and len_zero == 0:
                # only output neg.
                if len_neg == 1:
                    return list_pos[0] * list_pos[1] * list_neg[0]
                else:
                    return list_neg[-1] * list_neg[-2] * list_neg[-3]
            else:
                # can output pos.
                return list_pos[0] * list_neg[0] * list_neg[1]
        else:
            return 0




