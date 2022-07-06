"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/search-insert-position/
https://leetcode.com/problems/search-insert-position/discuss/2244599/Simple-Java-Solution-oror-100-Faster - check it


slice:
The slice() function returns a slice object that is used to slice any sequence (string, tuple, list, range, or bytes).
"""
from typing import List


class Solution:
    def searchInsert(self,
                     nums: List[int],
                     target: int) -> int:
        if not nums:
            return 0
        middle_index = len(nums) // 2
        middle_value = nums[middle_index]

        if target == middle_value:
            return middle_index
        elif len(nums) == 1:
            return 0 if target < middle_value else 1
        elif target < middle_value:
            return Solution().searchInsert(nums=nums[:middle_index], target=target)
        else:
            res = Solution().searchInsert(nums=nums[middle_index + 1:], target=target)
            return middle_index + res + 1


if __name__ == '__main__':
    result = Solution().searchInsert(nums=[5], target=5)
    assert result == 0, result
    result = Solution().searchInsert(nums=[15], target=5)
    assert result == 0, result
    result = Solution().searchInsert(nums=[3], target=5)
    assert result == 1, result
    result = Solution().searchInsert(nums=[1, 3, 5, 6, 9, 15, 21], target=5)
    assert result == 2, result
    result = Solution().searchInsert(nums=[1, 3, 5], target=4)
    assert result == 2, result
    result = Solution().searchInsert(nums=[1, 3, 5], target=6)
    assert result == 3, result
    result = Solution().searchInsert(nums=[1, 3, 5, 6], target=5)
    assert result == 2, result
    result = Solution().searchInsert(nums=[1, 3], target=4)
    assert result == 2, result
