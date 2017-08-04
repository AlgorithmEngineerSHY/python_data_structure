'''
For a web developer, it is very important to know how to design a web page's size. 
So, given a specific rectangular web page’s area, 
your job by now is to design a rectangular web page, 
whose length L and width W satisfy the following requirements:
'''
class Solution(object):
    def constructRectangle(self, area):
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1