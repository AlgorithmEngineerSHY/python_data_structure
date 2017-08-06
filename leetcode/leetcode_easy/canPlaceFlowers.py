'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, 
where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = ''.join([str(i) for i in [1, 0] + flowerbed + [0, 1]]).split('1')
        return sum(map(self.nmsl, flowerbed)) >= n

    def nmsl(self, x):
        len_x = len(x)
        if len_x < 3:
            return 0
        if (len_x - 2) % 2 == 0:
            return (len_x - 2) // 2
        else:
            return (len_x - 2) // 2 + 1
