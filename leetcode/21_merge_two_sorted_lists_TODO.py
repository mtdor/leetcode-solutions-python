"""
https://leetcode.com/problems/merge-two-sorted-lists/
https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained - check it
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_el=None):
        self.val = val
        self.next_el = next_el


# class Solution:
#     def mergeTwoLists(self,
#                       list1: List[int],
#                       list2: List[int]) -> List[int]:
#         result_list = []
#         counter1 = 0
#         counter2 = 0
#         while len(result_list) != len(list1) + len(list2):
#             el1 = list1[counter1]
#             el2 = list2[counter2]
#
#             if el1 <= el2:
#                 result_list.append(el1)
#                 counter1 += 1 if counter1 < len(list1) - 1 else 0
#                 # counter1
#             else:
#                 result_list.append(el2)
#                 counter2 += 1 if counter2 < len(list1) - 1 else 0
#                 # counter2
#
#             # print(len(result_list), len(list1), len(list2))
#
#         return result_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    l1n0 = ListNode(1)
    l1n1 = ListNode(2)
    l1n2 = ListNode(4)

    l2n0 = ListNode(1)
    l2n1 = ListNode(3)
    l2n2 = ListNode(4)

    result = Solution().mergeTwoLists(list1=l1n0, list2=l2n0)
    assert result == [1, 1, 2, 3, 4, 4], result
