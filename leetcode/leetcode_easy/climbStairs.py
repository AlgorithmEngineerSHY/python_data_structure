'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_2 = int(n/2)
        num = 0
        for i in range(n_2 + 1):
            n_1 = n - i * 2
            num += self.allSort(i, n_1)
            print(i, n_1, num)
        return num



    def factorial(self, n):
        num = 1
        for i in range(1, n + 1):
            num *= i
        return num

    def allSort(self, m, n):
        num = 1
        for i in range(n):
            num *= m + 1 + i
        return num / self.factorial(n)





















