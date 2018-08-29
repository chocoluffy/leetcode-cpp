"""
Input: 5
Output: [0,1,1,2,1,2]

5 = 4 + 1

Input: 7
Output: [0,1,1,2,1,2,2,3]

7 = 4 + 2 + 1

=> CB[i] = 1 + CB[i - closest 2 exponent value]

closest 2 exponenet value = 2 * floor(log base 2(element))

"""
import math
class Solution(object):
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        res = [0] * (num + 1)
        res[0] = 0
        res[1] = 1
        for i in range(2, num+1):
            closest_2_exp = 2 ** int(math.floor(math.log(i, 2)))
            # print i, closest_2_exp
            res[i] = 1 + res[i - closest_2_exp]
        return res


print Solution().countBits(5)

        