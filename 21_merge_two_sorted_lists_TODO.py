"""
https://leetcode.com/problems/merge-two-sorted-lists/
https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained - check it
"""

from typing import Optional, List

# Definition for singly-linked list.
from helpers.trees import is_identical


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'

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
        root_node = ListNode()
        curr_node = root_node
        while list1 or list2:
            l1_val = list1.val if list1 else None
            l2_val = list2.val if list2 else None

            new_node = ListNode()
            if list1 is None:
                new_node.val = l2_val
                list2 = list2.next
            elif list2 is None:
                new_node.val = l1_val
                list1 = list1.next
            elif l1_val < l2_val:
                new_node.val = l1_val
                list1 = list1.next
            else:
                new_node.val = l2_val
                list2 = list2.next
            curr_node.next = new_node
            curr_node = new_node

        return root_node.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))

    l2 = ListNode(1, ListNode(3, ListNode(4)))

    result = Solution().mergeTwoLists(l1, l2)
    print(result)
