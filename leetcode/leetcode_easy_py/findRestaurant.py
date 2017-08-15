'''
Suppose Andy and Doris want to choose a restaurant for dinner, 
and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement. 
You could assume there always exists an answer. 
'''
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set_1_2 = set(list1).intersection(set(list2))
        dict_1 = dict([(j, i) for i, j in enumerate(list1) if j in set_1_2])
        dict_2 = dict([(j, i) for i, j in enumerate(list2) if j in set_1_2])
        min_num = 2000
        r = []
        for i in set_1_2:
            tmp = dict_1[i] + dict_2[i]
            if tmp < min_num:
                min_num = tmp
                r = [i]
                continue
            if tmp == min_num:
                r.append(i)
        return r
