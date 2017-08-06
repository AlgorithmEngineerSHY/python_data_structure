'''
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.
'''
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = [1.0 * x for x in heaters]
        houses += heaters
        heaters.append(2**31 - 1.0)
        heaters.insert(0, -2**31 * 1.0)
        heaters.sort()
        houses.sort()
        radius = 0
        n = 0
        for i, j in enumerate(houses):
            if type(j) is not float:
                radius = max(min(abs(j - heaters[n]), abs(j - heaters[n + 1])), radius)
            else:
                n += 1
        return int(radius)
'''
        radius = 0
        for i in houses:
            tmp = min([abs(x - i) for x in heaters])
            if tmp > radius:
                radius = tmp
        return radius
'''

