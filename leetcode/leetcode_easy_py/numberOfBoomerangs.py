import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        nums = 0
        for x, y in points:
            counter = collections.Counter()
            for x_, y_ in points:
                counter[(x - x_)**2 + (y - y_)**2] += 1
            nums += sum([x * (x - 1) for x in counter.values()])
        return nums
