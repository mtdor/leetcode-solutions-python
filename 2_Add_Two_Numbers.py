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


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root_node: ListNode = ListNode()
        curr_node = root_node
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            nodes_sum = l1_val + l2_val + carry
            val = nodes_sum % 10
            carry = nodes_sum // 10
            new_node = ListNode(val)
            curr_node.next = new_node
            curr_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return root_node.next


if __name__ == '__main__':
    print(ListNode())
    # list1 = ListNode(2, ListNode(4, ListNode(3)))
    list1 = ListNode(6, ListNode(8))
    # list1 = ListNode(2)
    print('l1', list1)
    # list2 = ListNode(5, ListNode(6, ListNode(4)))
    list2 = ListNode(4, ListNode(1))
    # list2 = ListNode(5)
    print('l2', list2)
    list3: ListNode = Solution().addTwoNumbers(list1, list2)
    print('l3', list3)
