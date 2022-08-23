"""
https://leetcode.com/problems/palindrome-linked-list/

Approach 1:

Algorithm TODO:
* Copying the Linked List into an Array.
* Checking whether or not the Array is a palindrome using the two-pointer technique.

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, {self.next}'


class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]


# use the two-pointer technique
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]


Solution = Solution1

if __name__ == '__main__':
    assert Solution().isPalindrome(ListNode(1, ListNode(2))) is False
    assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(1)))) is True
