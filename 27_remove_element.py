"""
task: https://leetcode.com/problems/remove-element/
algorithm: https://en.wikipedia.org/wiki/In-place_algorithm
https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms
In computer science, an in-place algorithm
is an algorithm which transforms input using no auxiliary data structure.

Sometimes, I suck at easy questions))
"""

from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[count] = nums[i]
#                 count += 1
#         return count
class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == '__main__':
    nums_orig = [1, 2, 2, 3]
    k = Solution().removeElement(nums=nums_orig, val=3)
    print('nums_orig', k, nums_orig)
    # assert nums_orig == [2, 2, "_", "_"], nums_orig
