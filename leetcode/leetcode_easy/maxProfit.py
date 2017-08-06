'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
'''


class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1 or len(prices) == 0:
            return 0
        gradient_prices = []
        for i in range(len(prices) - 1):
            gradient_prices.append(prices[i + 1] - prices[i])
        max_sum = gradient_prices[0]
        tmp_sum = 0
        for i in gradient_prices:
            tmp_sum += i
            if tmp_sum < 0:
                tmp_sum = 0
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum


    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1 or len(prices) == 0:
            return 0
        gradient_prices = []
        for i in range(len(prices) - 1):
            gradient_prices.append(prices[i + 1] - prices[i])
        result = self.maxSubString(gradient_prices)
        if result < 0:
            return 0
        else:
            return result



    def maxSubString(self, string):
        length = len(string)
        if length == 1:
            return string[0]
        mid = length//2
        left_max_str = self.maxSubString(string[0: mid])
        right_max_str = self.maxSubString(string[mid:])
        mid_max_str = self.midMaxString(string, mid)

        if left_max_str >= right_max_str and left_max_str >= mid_max_str:
            return left_max_str
        elif right_max_str >= left_max_str and right_max_str >= mid_max_str:
            return right_max_str
        else:
            return mid_max_str


    def midMaxString(self, string, mid):
        #sum_ = string[mid - 1] + string[mid]
        max_right_sum = string[mid]
        tmp_right_sum = 0
        for i in string[mid:]:
            tmp_right_sum += i
            if tmp_right_sum > max_right_sum:
                max_right_sum = tmp_right_sum
        max_left_sum = string[mid - 1]
        tmp_left_sum = 0
        for i in string[mid - 1:: -1]:
            tmp_left_sum += i
            if tmp_left_sum > max_left_sum:
                max_left_sum = tmp_left_sum
        return max_left_sum + max_right_sum


