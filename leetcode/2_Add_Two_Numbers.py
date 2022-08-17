"""
https://leetcode.com/problems/add-two-numbers/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'
        # return f'{self.val}'


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_tree: ListNode = ListNode()
        curr_node = result_tree
        carry = 0
        while l1 or l2:
            nodes_sum = l1.val + l2.val + carry
            curr_node.val = nodes_sum % 10
            carry = nodes_sum // 10
            l1, l2 = l1.next, l2.next
            new_node = ListNode()
            curr_node.next = new_node
            curr_node = new_node
            # result = l1_val
        return result_tree


if __name__ == '__main__':
    print(ListNode())
    # list1 = ListNode(2, ListNode(4, ListNode(3)))
    list1 = ListNode(5, ListNode(6))
    # list1 = ListNode(2)
    print('l1', list1)
    # list2 = ListNode(5, ListNode(6, ListNode(4)))
    # list2 = ListNode(5)
    list2 = ListNode(9, ListNode(2))
    print('l2', list2)
    list3: ListNode = Solution().addTwoNumbers(list1, list2)
    print('l3', list3)
