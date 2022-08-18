"""
https://leetcode.com/problems/single-number/

explanation:
https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Explained
https://leetcode.com/problems/single-number/discuss/1771791/Python3-ONE-LINER-**-Explained
https://www.youtube.com/watch?v=myW_9B9T_II
https://www.pythonpool.com/python-xor/


https://www.geeksforgeeks.org/reduce-in-python/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor

"""
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


if __name__ == '__main__':
    assert 1 ^ 1 == 0
    assert 2 ^ 2 == 0
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
    # print(Solution().singleNumber([4, 1, 2, 1, 2, 3, 8]))
